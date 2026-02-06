const std = @import("std");
const rl = @import("local_raylib.zig").rl;
const Physics = @import("physics.zig").Physics;

pub const Tautris = struct {
    grid: [20][10][10]bool,
    current_piece: Piece,
    position: [3]i32,
    rotation: u8,
    locked_blocks: std.array_list.Managed([3]i32),
    piece_locked: bool,
    score: u32,
    drop_timer: f32,
    drop_interval: f32,

    const Piece = enum {
        I,
        O,
        T,
        S,
        Z,
        J,
        L,

        pub fn getBlocks(self: Piece) [4][3]i32 {
            return switch (self) {
                .I => [4][3]i32{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 3, 0, 0 } },
                .O => [4][3]i32{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 0, 0, 1 }, .{ 1, 0, 1 } },
                .T => [4][3]i32{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 1, 0, 1 } },
                .S => [4][3]i32{ .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 0, 0, 1 }, .{ 1, 0, 1 } },
                .Z => [4][3]i32{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 1, 0, 1 }, .{ 2, 0, 1 } },
                .J => [4][3]i32{ .{ 0, 0, 0 }, .{ 0, 0, 1 }, .{ 0, 0, 2 }, .{ 1, 0, 2 } },
                .L => [4][3]i32{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 1, 0, 1 }, .{ 1, 0, 2 } },
            };
        }

        pub fn getColor(self: Piece) rl.Color {
            const color: rl.Color = switch (self) {
                .I => rl.SKYBLUE,
                .O => rl.YELLOW,
                .T => rl.PURPLE,
                .S => rl.GREEN,
                .Z => rl.RED,
                .J => rl.BLUE,
                .L => rl.ORANGE,
            };

            return color;
        }
    };

    pub fn init() Tautris {
        var gpa = std.heap.GeneralPurposeAllocator(.{}){};
        const allocator = gpa.allocator();

        return Tautris{
            .grid = [_][10][10]bool{[_][10]bool{[_]bool{false} ** 10} ** 10} ** 20,
            .current_piece = .T,
            .position = .{ 4, 18, 4 },
            .rotation = 0,
            .locked_blocks = std.array_list.Managed([3]i32).init(allocator),
            .piece_locked = false,
            .score = 0,
            .drop_timer = 0,
            .drop_interval = 1.0,
        };
    }

    pub fn update(self: *Tautris, dt: f32, physics: *Physics) void {
        _ = physics; // Gravity not actually used yet

        self.drop_timer += dt;
        if (self.drop_timer >= self.drop_interval) {
            self.drop_timer = 0;
            self.moveDown();
        }
    }

    pub fn handleInput(self: *Tautris) void {
        // Qwerty
        if (true) {
            if (rl.IsKeyPressed(rl.KEY_A) or rl.IsKeyPressed(rl.KEY_LEFT)) self.moveLeft();
            if (rl.IsKeyPressed(rl.KEY_D) or rl.IsKeyPressed(rl.KEY_RIGHT)) self.moveRight();
            if (rl.IsKeyPressed(rl.KEY_W) or rl.IsKeyPressed(rl.KEY_UP)) self.moveForward();
            if (rl.IsKeyPressed(rl.KEY_S)) self.moveBackward();
        } else {
            if (rl.IsKeyPressed(rl.KEY_A) or rl.IsKeyPressed(rl.KEY_LEFT)) self.moveLeft();
            if (rl.IsKeyPressed(rl.KEY_E) or rl.IsKeyPressed(rl.KEY_RIGHT)) self.moveRight();
            if (rl.IsKeyPressed(rl.KEY_COMMA) or rl.IsKeyPressed(rl.KEY_UP)) self.moveForward();
            if (rl.IsKeyPressed(rl.KEY_O)) self.moveBackward();
        }

        if (rl.IsKeyPressed(rl.KEY_DOWN)) self.hardDrop();
        if (rl.IsKeyPressed(rl.KEY_SPACE)) self.rotate();
    }

    fn moveLeft(self: *Tautris) void {
        self.position[0] -= 1;
        if (self.checkCollision()) self.position[0] += 1;
    }

    fn moveRight(self: *Tautris) void {
        self.position[0] += 1;
        if (self.checkCollision()) self.position[0] -= 1;
    }

    fn moveForward(self: *Tautris) void {
        self.position[2] -= 1;
        if (self.checkCollision()) self.position[2] += 1;
    }

    fn moveBackward(self: *Tautris) void {
        self.position[2] += 1;
        if (self.checkCollision()) self.position[2] -= 1;
    }

    fn moveDown(self: *Tautris) void {
        self.position[1] -= 1;
        if (self.checkCollision()) {
            self.position[1] += 1;
            self.lockPiece();
        }
    }

    fn hardDrop(self: *Tautris) void {
        while (!self.checkCollision()) {
            self.position[1] -= 1;
        }
        self.position[1] += 1;
        self.lockPiece();
    }

    fn rotate(self: *Tautris) void {
        self.rotation = (self.rotation + 1) % 4;
        if (self.checkCollision()) {
            self.rotation = (self.rotation + 3) % 4;
        }
    }

    fn checkCollision(self: *Tautris) bool {
        const blocks = self.current_piece.getBlocks();
        for (blocks) |block| {
            const x = self.position[0] + block[0];
            const y = self.position[1] + block[1];
            const z = self.position[2] + block[2];

            if (x < 0 or x >= 10 or z < 0 or z >= 10 or y < 0) return true;
            if (y >= 20) continue;
            if (self.grid[@intCast(y)][@intCast(x)][@intCast(z)]) return true;
        }
        return false;
    }

    fn lockPiece(self: *Tautris) void {
        const blocks = self.current_piece.getBlocks();
        for (blocks) |block| {
            const x = self.position[0] + block[0];
            const y = self.position[1] + block[1];
            const z = self.position[2] + block[2];

            if (y >= 0 and y < 20) {
                self.grid[@intCast(y)][@intCast(x)][@intCast(z)] = true;
                self.locked_blocks.append(.{ @intCast(x), @intCast(y), @intCast(z) }) catch {};
            }
        }

        self.piece_locked = true;
        self.clearLines();
        self.spawnPiece();
    }

    fn clearLines(self: *Tautris) void {
        var y: i32 = 0;
        while (y < 20) : (y += 1) {
            var full = true;
            var x: i32 = 0;
            while (x < 10) : (x += 1) {
                var z: i32 = 0;
                while (z < 10) : (z += 1) {
                    if (!self.grid[@intCast(y)][@intCast(x)][@intCast(z)]) {
                        full = false;
                        break;
                    }
                }
                if (!full) break;
            }

            if (full) {
                self.score += 100;
                // Shift down
                var yy = y;
                while (yy < 19) : (yy += 1) {
                    self.grid[@intCast(yy)] = self.grid[@intCast(yy + 1)];
                }
                self.grid[19] = [_][10]bool{[_]bool{false} ** 10} ** 10;
            }
        }
    }

    fn spawnPiece(self: *Tautris) void {
        const pieces = [_]Piece{ .I, .O, .T, .S, .Z, .J, .L };
        const idx = @mod(@as(usize, @intCast(rl.GetRandomValue(0, 6))), 7);
        self.current_piece = pieces[idx];
        self.position = .{ 4, 18, 4 };
        self.rotation = 0;
    }

    pub fn getCurrentBlocks(self: *Tautris) [4][3]i32 {
        const blocks = self.current_piece.getBlocks();
        var result: [4][3]i32 = undefined;
        for (blocks, 0..) |block, i| {
            result[i][0] = self.position[0] + block[0];
            result[i][1] = self.position[1] + block[1];
            result[i][2] = self.position[2] + block[2];
        }
        return result;
    }
};
