const std = @import("std");
const rl = @import("local_raylib.zig").rl;
const Physics = @import("physics.zig").Physics;
const KSpaceSubstrate = @import("kspace_substrate.zig").KSpaceSubstrate;
const math = std.math;

pub const Material = enum {
    stone,
    jello,
    mud,
    metal,
    glass,

    pub fn stiffness(self: Material) f32 {
        return switch (self) {
            .stone => 50.0, // N/m spring constant
            .jello => 2.0,
            .mud => 10.0,
            .metal => 100.0,
            .glass => 80.0,
        };
    }

    pub fn damping(self: Material) f32 {
        return switch (self) {
            .stone => 0.8,
            .jello => 0.95,
            .mud => 0.98,
            .metal => 0.7,
            .glass => 0.75,
        };
    }

    pub fn density(self: Material) f32 {
        return switch (self) {
            .stone => 2500.0, // kg/m³
            .jello => 1000.0,
            .mud => 1800.0,
            .metal => 7800.0,
            .glass => 2500.0,
        };
    }

    pub fn fracture_threshold(self: Material) f32 {
        return switch (self) {
            .stone => 15.0, // m/s impact velocity
            .jello => 1000.0,
            .mud => 1000.0,
            .metal => 25.0,
            .glass => 8.0,
        };
    }

    pub fn getColor(self: Material) rl.Color {
        return switch (self) {
            .stone => rl.Color{ .r = 128, .g = 128, .b = 128, .a = 255 },
            .jello => rl.Color{ .r = 255, .g = 100, .b = 100, .a = 200 },
            .mud => rl.Color{ .r = 139, .g = 69, .b = 19, .a = 255 },
            .metal => rl.Color{ .r = 192, .g = 192, .b = 192, .a = 255 },
            .glass => rl.Color{ .r = 200, .g = 230, .b = 255, .a = 150 },
        };
    }
};

pub const Voxel = struct {
    position: [3]f32,
    velocity: [3]f32,
    rest_position: [3]f32,
    mass: f32,
    material: Material,
    active: bool,
    size: f32, // Physical size in meters

    pub fn applyForce(self: *Voxel, force: [3]f32, dt: f32) void {
        const accel = [3]f32{
            force[0] / self.mass,
            force[1] / self.mass,
            force[2] / self.mass,
        };

        self.velocity[0] += accel[0] * dt;
        self.velocity[1] += accel[1] * dt;
        self.velocity[2] += accel[2] * dt;
    }

    pub fn integrate(self: *Voxel, dt: f32, damping: f32) void {
        self.position[0] += self.velocity[0] * dt;
        self.position[1] += self.velocity[1] * dt;
        self.position[2] += self.velocity[2] * dt;

        self.velocity[0] *= damping;
        self.velocity[1] *= damping;
        self.velocity[2] *= damping;
    }
};

pub const SoftBody = struct {
    voxels: std.array_list.Managed(Voxel),
    material: Material,
    center_of_mass: [3]f32,
    is_player_controlled: bool,

    pub fn init(allocator: std.mem.Allocator, blocks: [4][3]i32, position: [3]f32, material: Material) !SoftBody {
        var voxels = std.array_list.Managed(Voxel).init(allocator);

        const voxel_size: f32 = 0.5; // Each block is 0.5m = 50cm cube
        const voxel_volume = voxel_size * voxel_size * voxel_size; // m³
        const voxel_mass = material.density() * voxel_volume; // kg

        for (blocks) |block| {
            try voxels.append(Voxel{
                .position = .{
                    position[0] + @as(f32, @floatFromInt(block[0])) * voxel_size,
                    position[1] + @as(f32, @floatFromInt(block[1])) * voxel_size,
                    position[2] + @as(f32, @floatFromInt(block[2])) * voxel_size,
                },
                .velocity = .{ 0, 0, 0 },
                .rest_position = .{
                    @as(f32, @floatFromInt(block[0])) * voxel_size,
                    @as(f32, @floatFromInt(block[1])) * voxel_size,
                    @as(f32, @floatFromInt(block[2])) * voxel_size,
                },
                .mass = voxel_mass,
                .material = material,
                .active = true,
                .size = voxel_size,
            });
        }

        return SoftBody{
            .voxels = voxels,
            .material = material,
            .center_of_mass = position,
            .is_player_controlled = true,
        };
    }

    pub fn updatePhysics(self: *SoftBody, dt: f32, gravity: f32, physics: *Physics) void {
        _ = physics;
        _ = gravity; // Using real Earth gravity instead

        const earth_gravity: f32 = 9.81; // m/s²
        const stiff = self.material.stiffness();
        const damp = self.material.damping();

        // Apply gravity
        for (self.voxels.items) |*voxel| {
            if (!voxel.active) continue;
            voxel.applyForce(.{ 0, -earth_gravity * voxel.mass, 0 }, dt);
        }

        // Spring forces (shape preservation)
        var i: usize = 0;
        while (i < self.voxels.items.len) : (i += 1) {
            if (!self.voxels.items[i].active) continue;

            var j: usize = i + 1;
            while (j < self.voxels.items.len) : (j += 1) {
                if (!self.voxels.items[j].active) continue;

                const v1 = &self.voxels.items[i];
                const v2 = &self.voxels.items[j];

                // Rest distance
                const dx_rest = v1.rest_position[0] - v2.rest_position[0];
                const dy_rest = v1.rest_position[1] - v2.rest_position[1];
                const dz_rest = v1.rest_position[2] - v2.rest_position[2];
                const rest_dist = @sqrt(dx_rest * dx_rest + dy_rest * dy_rest + dz_rest * dz_rest);

                if (rest_dist < 0.01) continue;

                // Current distance
                const dx = v1.position[0] - v2.position[0];
                const dy = v1.position[1] - v2.position[1];
                const dz = v1.position[2] - v2.position[2];
                const dist = @sqrt(dx * dx + dy * dy + dz * dz);

                if (dist < 0.001) continue;

                // Spring force: F = k * Δx
                const displacement = dist - rest_dist;
                const force_mag = stiff * displacement;
                const force = [3]f32{
                    (dx / dist) * force_mag,
                    (dy / dist) * force_mag,
                    (dz / dist) * force_mag,
                };

                v1.applyForce(.{ -force[0], -force[1], -force[2] }, dt);
                v2.applyForce(.{ force[0], force[1], force[2] }, dt);
            }
        }

        // Integrate
        for (self.voxels.items) |*voxel| {
            if (!voxel.active) continue;
            voxel.integrate(dt, damp);
        }

        self.updateCenterOfMass();
    }

    pub fn handleCollisions(self: *SoftBody, floor_y: f32) void {
        const restitution: f32 = 0.3; // Coefficient of restitution (bounciness)
        const friction: f32 = 0.8;

        for (self.voxels.items) |*voxel| {
            if (!voxel.active) continue;

            const half_size = voxel.size * 0.5;

            // Floor collision
            if (voxel.position[1] - half_size < floor_y) {
                voxel.position[1] = floor_y + half_size;
                voxel.velocity[1] = -voxel.velocity[1] * restitution;

                // Friction
                voxel.velocity[0] *= friction;
                voxel.velocity[2] *= friction;
            }

            // Wall collisions (10m × 10m play area)
            if (voxel.position[0] - half_size < 0) {
                voxel.position[0] = half_size;
                voxel.velocity[0] = -voxel.velocity[0] * restitution;
            }
            if (voxel.position[0] + half_size > 10) {
                voxel.position[0] = 10 - half_size;
                voxel.velocity[0] = -voxel.velocity[0] * restitution;
            }
            if (voxel.position[2] - half_size < 0) {
                voxel.position[2] = half_size;
                voxel.velocity[2] = -voxel.velocity[2] * restitution;
            }
            if (voxel.position[2] + half_size > 10) {
                voxel.position[2] = 10 - half_size;
                voxel.velocity[2] = -voxel.velocity[2] * restitution;
            }
        }
    }

    pub fn checkFracture(self: *SoftBody, physics: *Physics) bool {
        _ = physics;
        const threshold = self.material.fracture_threshold();

        for (self.voxels.items) |*voxel| {
            if (!voxel.active) continue;

            const speed = @sqrt(voxel.velocity[0] * voxel.velocity[0] +
                voxel.velocity[1] * voxel.velocity[1] +
                voxel.velocity[2] * voxel.velocity[2]);

            if (speed > threshold) {
                return true;
            }
        }

        return false;
    }

    pub fn fracture(self: *SoftBody) void {
        // Fracture: disable random voxels
        for (self.voxels.items) |*voxel| {
            if (rl.GetRandomValue(0, 3) == 0) {
                voxel.active = false;
            }
        }
    }

    fn updateCenterOfMass(self: *SoftBody) void {
        var sum_x: f32 = 0;
        var sum_y: f32 = 0;
        var sum_z: f32 = 0;
        var count: f32 = 0;

        for (self.voxels.items) |voxel| {
            if (!voxel.active) continue;
            sum_x += voxel.position[0];
            sum_y += voxel.position[1];
            sum_z += voxel.position[2];
            count += 1;
        }

        if (count > 0) {
            self.center_of_mass = .{
                sum_x / count,
                sum_y / count,
                sum_z / count,
            };
        }
    }

    pub fn applyPlayerControl(self: *SoftBody, force: [3]f32) void {
        if (!self.is_player_controlled) return;

        for (self.voxels.items) |*voxel| {
            if (!voxel.active) continue;
            voxel.velocity[0] += force[0];
            voxel.velocity[1] += force[1];
            voxel.velocity[2] += force[2];
        }
    }
};

pub const Tautris = struct {
    bodies: std.array_list.Managed(SoftBody),
    current_body: ?usize,
    spawn_timer: f32,
    spawn_interval: f32,
    max_spawn_time: f32,
    allocator: std.mem.Allocator,
    score: u32,

    pub fn init(allocator: std.mem.Allocator) !Tautris {
        var tetris = Tautris{
            .bodies = std.array_list.Managed(SoftBody).init(allocator),
            .current_body = null,
            .spawn_timer = 0,
            .spawn_interval = 3.0,
            .max_spawn_time = 5.0,
            .allocator = allocator,
            .score = 0,
        };

        try tetris.spawnPiece();

        return tetris;
    }

    pub fn update(self: *Tautris, dt: f32, physics: *Physics) void {
        // Update all bodies
        for (self.bodies.items) |*body| {
            body.updatePhysics(dt, 0, physics);
            body.handleCollisions(0.0);

            if (body.checkFracture(physics)) {
                body.fracture();
            }
        }

        // Check if current piece has settled
        if (self.current_body) |idx| {
            const settled = self.bodies.items[idx].center_of_mass[1] < 0.5 and
                self.getBodyVelocitySquared(idx) < 0.5;

            const timeout = self.spawn_timer >= self.max_spawn_time;

            if (settled or timeout) {
                self.bodies.items[idx].is_player_controlled = false;
                self.spawn_timer = 0;
                self.current_body = null;
            }
        }

        // Spawn new piece
        if (self.current_body == null) {
            self.spawn_timer += dt;
            if (self.spawn_timer >= 0.5) {
                self.spawnPiece() catch {};
            }
        } else {
            self.spawn_timer += dt;
        }
    }

    pub fn handleInput(self: *Tautris) void {
        if (self.current_body) |idx| {
            var force = [3]f32{ 0, 0, 0 };
            const control_strength: f32 = 2.0; // Newtons of force

            if (rl.IsKeyDown(rl.KEY_A) or rl.IsKeyDown(rl.KEY_LEFT)) {
                force[0] = -control_strength;
            }
            if (rl.IsKeyDown(rl.KEY_D) or rl.IsKeyDown(rl.KEY_RIGHT)) {
                force[0] = control_strength;
            }
            if (rl.IsKeyDown(rl.KEY_W) or rl.IsKeyDown(rl.KEY_UP)) {
                force[2] = -control_strength;
            }
            if (rl.IsKeyDown(rl.KEY_S)) {
                force[2] = control_strength;
            }
            if (rl.IsKeyDown(rl.KEY_DOWN)) {
                force[1] = -control_strength * 3;
            }

            self.bodies.items[idx].applyPlayerControl(force);
        }
    }

    fn spawnPiece(self: *Tautris) !void {
        const pieces = [_][4][3]i32{
            .{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 3, 0, 0 } }, // I
            .{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 0, 0, 1 }, .{ 1, 0, 1 } }, // O
            .{ .{ 0, 0, 0 }, .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 1, 0, 1 } }, // T
            .{ .{ 1, 0, 0 }, .{ 2, 0, 0 }, .{ 0, 0, 1 }, .{ 1, 0, 1 } }, // S
        };

        const materials = [_]Material{ .stone, .jello, .mud, .metal, .glass };

        const piece_idx = @mod(@as(usize, @intCast(rl.GetRandomValue(0, 100))), pieces.len);
        const mat_idx = @mod(@as(usize, @intCast(rl.GetRandomValue(0, 100))), materials.len);

        const body = try SoftBody.init(
            self.allocator,
            pieces[piece_idx],
            .{ 5.0, 18.0, 5.0 }, // Spawn at center, high up
            materials[mat_idx],
        );

        // No initial velocity - let gravity do the work
        for (body.voxels.items) |*voxel| {
            voxel.velocity = .{ 0, 0, 0 };
        }

        try self.bodies.append(body);
        self.current_body = self.bodies.items.len - 1;
        self.spawn_timer = 0;
    }

    fn getBodyVelocitySquared(self: *Tautris, idx: usize) f32 {
        var sum: f32 = 0;
        var count: f32 = 0;
        for (self.bodies.items[idx].voxels.items) |voxel| {
            if (!voxel.active) continue;
            sum += voxel.velocity[0] * voxel.velocity[0] +
                voxel.velocity[1] * voxel.velocity[1] +
                voxel.velocity[2] * voxel.velocity[2];
            count += 1;
        }
        if (count == 0) return 0;
        return sum / count;
    }

    pub fn updateSubstrateCoupling(self: *Tautris, substrate: *KSpaceSubstrate, physics: *Physics) void {
        const scale = @as(f32, @floatCast(physics.holographic_scale() * 50.0));

        for (self.bodies.items) |*body| {
            for (body.voxels.items) |voxel| {
                if (!voxel.active) continue;

                const kx = @as(i32, @intFromFloat(voxel.position[0] * scale));
                const ky = @as(i32, @intFromFloat(voxel.position[2] * scale));

                if (kx >= 0 and kx < substrate.size and ky >= 0 and ky < substrate.size) {
                    const idx = @as(usize, @intCast(ky * substrate.size + kx));

                    const speed = @sqrt(voxel.velocity[0] * voxel.velocity[0] +
                        voxel.velocity[1] * voxel.velocity[1] +
                        voxel.velocity[2] * voxel.velocity[2]);
                    substrate.data[idx] += speed * 0.002;
                }
            }
        }
    }
};
