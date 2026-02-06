const std = @import("std");
const rl = @cImport({
    @cInclude("raylib.h");
});
const math = std.math;
const KSpaceSubstrate = @import("kspace_substrate.zig").KSpaceSubstrate;
const Physics = @import("physics.zig").Physics;
const Tautris = @import("tautris.zig").Tautris;

pub const Renderer = struct {
    camera: rl.Camera3D,

    pub fn init() Renderer {
        return Renderer{
            .camera = rl.Camera3D{
                .position = .{ .x = 15, .y = 25, .z = 15 },
                .target = .{ .x = 5, .y = 10, .z = 5 },
                .up = .{ .x = 0, .y = 1, .z = 0 },
                .fovy = 45,
                .projection = rl.CAMERA_PERSPECTIVE,
            },
        };
    }

    pub fn renderKSpace(
        self: *Renderer,
        substrate: *KSpaceSubstrate,
        x: i32,
        y: i32,
        width: i32,
        height: i32,
    ) void {
        _ = self;

        const sx_step = @as(i32, @intFromFloat(@as(f32, @floatFromInt(substrate.size)) / @as(f32, @floatFromInt(width))));
        const sy_step = @as(i32, @intFromFloat(@as(f32, @floatFromInt(substrate.size)) / @as(f32, @floatFromInt(height))));

        var py: i32 = 0;
        while (py < height) : (py += 1) {
            var px: i32 = 0;
            while (px < width) : (px += 1) {
                const sx = @min(px * sx_step, substrate.size - 1);
                const sy = @min(py * sy_step, substrate.size - 1);

                const value = substrate.getValue(sx, sy);
                const color = colormapDisplacement(value);
                rl.DrawPixel(x + px, y + py, color);
            }
        }
    }

    pub fn renderTautris3D(
        self: *Renderer,
        tautris: *Tautris,
        physics: *Physics,
        x: i32,
        y: i32,
        width: i32,
        height: i32,
    ) void {
        _ = physics;

        // Set viewport for this panel
        rl.BeginScissorMode(x, y, width, height);
        defer rl.EndScissorMode();

        rl.BeginMode3D(self.camera);
        defer rl.EndMode3D();

        // Draw grid floor
        rl.DrawGrid(20, 1.0);

        // Draw locked blocks
        var yy: i32 = 0;
        while (yy < 20) : (yy += 1) {
            var xx: i32 = 0;
            while (xx < 10) : (xx += 1) {
                var zz: i32 = 0;
                while (zz < 10) : (zz += 1) {
                    if (tautris.grid[@intCast(yy)][@intCast(xx)][@intCast(zz)]) {
                        const pos = rl.Vector3{
                            .x = @floatFromInt(xx),
                            .y = @floatFromInt(yy),
                            .z = @floatFromInt(zz),
                        };
                        rl.DrawCube(pos, 0.9, 0.9, 0.9, rl.GRAY);
                        rl.DrawCubeWires(pos, 1.0, 1.0, 1.0, rl.DARKGRAY);
                    }
                }
            }
        }

        // Draw current piece
        const blocks = tautris.getCurrentBlocks();
        const color = tautris.current_piece.getColor();
        for (blocks) |block| {
            const pos = rl.Vector3{
                .x = @floatFromInt(block[0]),
                .y = @floatFromInt(block[1]),
                .z = @floatFromInt(block[2]),
            };
            rl.DrawCube(pos, 0.9, 0.9, 0.9, color);
            rl.DrawCubeWires(pos, 1.0, 1.0, 1.0, rl.BLACK);
        }

        // Draw bounds
        rl.DrawCubeWires(
            rl.Vector3{ .x = 5, .y = 10, .z = 5 },
            10,
            20,
            10,
            rl.WHITE,
        );
    }

    pub fn renderXSpace(
        self: *Renderer,
        substrate: *KSpaceSubstrate,
        physics: *Physics,
        x: i32,
        y: i32,
        width: i32,
        height: i32,
    ) void {
        _ = self;
        _ = physics;

        // Simplified x-space: just show substrate with different colormap
        const sx_step = @as(i32, @intFromFloat(@as(f32, @floatFromInt(substrate.size)) / @as(f32, @floatFromInt(width))));
        const sy_step = @as(i32, @intFromFloat(@as(f32, @floatFromInt(substrate.size)) / @as(f32, @floatFromInt(height))));

        var py: i32 = 0;
        while (py < height) : (py += 1) {
            var px: i32 = 0;
            while (px < width) : (px += 1) {
                const sx = @min(px * sx_step, substrate.size - 1);
                const sy = @min(py * sy_step, substrate.size - 1);

                const value = substrate.getValue(sx, sy);
                const color = colormapXSpace(value);
                rl.DrawPixel(x + px, y + py, color);
            }
        }
    }

    fn colormapDisplacement(value: f32) rl.Color {
        var normalized = (value + 2.0) / 4.0;
        normalized = math.clamp(normalized, 0.0, 1.0);

        if (normalized < 0.5) {
            const t = normalized * 2.0;
            return rl.Color{
                .r = @intFromFloat(t * 255.0),
                .g = @intFromFloat(t * 255.0),
                .b = 255,
                .a = 255,
            };
        } else {
            const t = (normalized - 0.5) * 2.0;
            return rl.Color{
                .r = 255,
                .g = @intFromFloat((1.0 - t) * 255.0),
                .b = @intFromFloat((1.0 - t) * 255.0),
                .a = 255,
            };
        }
    }

    fn colormapXSpace(value: f32) rl.Color {
        var normalized = (value + 2.0) / 4.0;
        normalized = math.clamp(normalized, 0.0, 1.0);

        const r: u8 = @intFromFloat(normalized * 255.0);
        return rl.Color{ .r = r, .g = r, .b = r, .a = 255 };
    }
};
