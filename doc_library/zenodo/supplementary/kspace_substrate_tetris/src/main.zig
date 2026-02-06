const std = @import("std");
const rl = @cImport({
    @cInclude("raylib.h");
});

const KSpaceSubstrate = @import("kspace_substrate.zig").KSpaceSubstrate;
const Physics = @import("physics.zig").Physics;
const Tetris = @import("tetris.zig").Tetris;
const Renderer = @import("renderer.zig").Renderer;
const UI = @import("ui.zig").UI;

pub fn main() !void {
    // App arena - never freed until exit
    var app_gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = app_gpa.deinit();
    var app_arena = std.heap.ArenaAllocator.init(app_gpa.allocator());
    defer app_arena.deinit();
    const app_allocator = app_arena.allocator();

    // Frame arena - reset every frame
    var frame_gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = frame_gpa.deinit();
    var frame_arena = std.heap.ArenaAllocator.init(frame_gpa.allocator());
    defer frame_arena.deinit();
    const frame_allocator = frame_arena.allocator();

    // Window setup
    const window_width: i32 = 1600;
    const window_height: i32 = 900;

    rl.SetConfigFlags(rl.FLAG_WINDOW_RESIZABLE | rl.FLAG_MSAA_4X_HINT);
    rl.InitWindow(window_width, window_height, "K-Space Physics Tetris");
    defer rl.CloseWindow();
    rl.SetTargetFPS(60);

    // Initialize systems
    var substrate = try KSpaceSubstrate.init(app_allocator, 512);
    var physics = Physics{ .N = 9e60 };
    var tetris = Tetris.init();
    var renderer = Renderer.init();
    var ui = UI.init();

    // Game state
    var mode: enum { kspace, xspace } = .kspace;
    var paused = false;
    var show_ui = true;

    // Main loop
    while (!rl.WindowShouldClose()) {
        const dt = rl.GetFrameTime();

        // Input handling
        if (rl.IsKeyPressed(rl.KEY_TAB)) {
            mode = if (mode == .kspace) .xspace else .kspace;
        }
        if (rl.IsKeyPressed(rl.KEY_F1)) {
            show_ui = !show_ui;
        }
        if (rl.IsKeyPressed(rl.KEY_SPACE)) {
            try saveScreenshot(app_allocator);
        }
        if (rl.IsKeyPressed(rl.KEY_P)) {
            paused = !paused;
        }

        // Update UI (slider changes N)
        ui.update(&physics);

        // Update game
        if (!paused) {
            tetris.update(dt, &physics);
            tetris.handleInput();
            
            // Update substrate when piece locks
            if (tetris.piece_locked) {
                substrate.injectPiece(tetris.locked_blocks, &physics);
                tetris.piece_locked = false;
            }
            
            substrate.step(dt, &physics);
        }

        // Render
        rl.BeginDrawing();
        defer rl.EndDrawing();
        rl.ClearBackground(rl.Color{ .r = 10, .g = 10, .b = 15, .a = 255 });

        const screen_width = rl.GetScreenWidth();
        const screen_height = rl.GetScreenHeight();

        if (mode == .kspace) {
            // K-space mode: left panel = substrate, center = tetris, right = substrate zoom
            renderer.renderKSpace(&substrate, 0, 0, screen_width / 3, screen_height);
            renderer.renderTetris3D(&tetris, &physics, screen_width / 3, 0, screen_width / 3, screen_height);
            renderer.renderKSpace(&substrate, 2 * screen_width / 3, 0, screen_width / 3, screen_height);
        } else {
            // X-space mode: left = xspace, center = tetris, right = physics info
            renderer.renderXSpace(&substrate, &physics, 0, 0, screen_width / 3, screen_height);
            renderer.renderTetris3D(&tetris, &physics, screen_width / 3, 0, screen_width / 3, screen_height);
            renderer.renderXSpace(&substrate, &physics, 2 * screen_width / 3, 0, screen_width / 3, screen_height);
        }

        // UI overlay
        if (show_ui) {
            ui.render(&physics, &tetris, mode);
        }

        // FPS
        var buffer: [64]u8 = undefined;
        const fps_text = std.fmt.bufPrintZ(&buffer, "FPS: {d}", .{rl.GetFPS()}) catch "FPS";
        rl.DrawText(fps_text.ptr, screen_width - 100, 10, 20, rl.LIME);

        // Reset frame arena
        _ = frame_arena.reset(.retain_capacity);
    }
}

fn saveScreenshot(allocator: std.mem.Allocator) !void {
    const prefix = "kspace_tetris_";
    const ext = ".png";

    var dir = std.fs.cwd();
    var counter: u32 = 0;
    
    while (counter < 10000) : (counter += 1) {
        const filename = try std.fmt.allocPrintZ(
            allocator,
            "{s}{d:0>4}{s}",
            .{ prefix, counter, ext },
        );
        
        const file = dir.openFile(filename, .{}) catch {
            rl.TakeScreenshot(filename.ptr);
            std.debug.print("Saved: {s}\n", .{filename});
            return;
        };
        file.close();
    }
}

