const std = @import("std");
const rl = @cImport({
    @cInclude("raylib.h");
});
const Physics = @import("physics.zig").Physics;
const Tetris = @import("tetris.zig").Tetris;
const math = std.math;

pub const UI = struct {
    n_slider_value: f32,

    pub fn init() UI {
        return UI{
            .n_slider_value = 60.0, // log scale: 10^60
        };
    }

    pub fn update(self: *UI, physics: *Physics) void {
        // Handle N slider with mouse wheel
        if (rl.IsKeyDown(rl.KEY_N)) {
            const wheel = rl.GetMouseWheelMove();
            self.n_slider_value += wheel * 0.5;
            self.n_slider_value = math.clamp(self.n_slider_value, 50.0, 70.0);
        }

        physics.N = math.pow(f64, 10.0, self.n_slider_value);
    }

    pub fn render(
        self: *UI,
        physics: *Physics,
        tetris: *Tetris,
        mode: anytype,
    ) void {
        var buffer: [256]u8 = undefined;

        // Top left: Physics info
        var text = std.fmt.bufPrintZ(&buffer, "N = 10^{d:.1f}", .{self.n_slider_value}) catch "N";
        rl.DrawText(text.ptr, 10, 10, 20, rl.LIME);

        text = std.fmt.bufPrintZ(&buffer, "α⁻¹ = {d:.3f}", .{physics.alpha_em_inv()}) catch "α";
        rl.DrawText(text.ptr, 10, 35, 18, rl.WHITE);

        text = std.fmt.bufPrintZ(&buffer, "αg = {e:.2}", .{physics.alpha_g()}) catch "αg";
        rl.DrawText(text.ptr, 10, 60, 18, rl.WHITE);

        text = std.fmt.bufPrintZ(&buffer, "ρΛ = {e:.2}", .{physics.dark_energy()}) catch "ρΛ";
        rl.DrawText(text.ptr, 10, 85, 18, rl.WHITE);

        // Game info
        text = std.fmt.bufPrintZ(&buffer, "Score: {d}", .{tetris.score}) catch "Score";
        rl.DrawText(text.ptr, 10, 130, 20, rl.YELLOW);

        // Mode indicator
        const mode_text = if (mode == .kspace) "K-SPACE" else "X-SPACE";
        rl.DrawText(mode_text, 10, 170, 24, rl.ORANGE);

        // Controls
        const help_y = rl.GetScreenHeight() - 120;
        rl.DrawText("Controls:", 10, help_y, 18, rl.LIGHTGRAY);
        rl.DrawText("WASD: Move | Arrows: Rotate", 10, help_y + 25, 16, rl.GRAY);
        rl.DrawText("Down: Drop | TAB: Mode | P: Pause", 10, help_y + 45, 16, rl.GRAY);
        rl.DrawText("N+Wheel: Adjust N | Space: Screenshot", 10, help_y + 65, 16, rl.GRAY);
        rl.DrawText("F1: Toggle UI", 10, help_y + 85, 16, rl.GRAY);
    }
};

