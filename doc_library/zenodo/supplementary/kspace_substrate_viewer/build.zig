const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const exe = b.addExecutable(.{
        .name = "substrate_viewer",
        .root_module = b.createModule(.{
            .root_source_file = b.path("src/substrate_viewer.zig"),
            .target = target,
            .optimize = optimize,
        })
    });

    // Link raylib
    exe.linkSystemLibrary("raylib");
    exe.linkLibC();

    b.installArtifact(exe);

    const run_cmd = b.addRunArtifact(exe);
    run_cmd.step.dependOn(b.getInstallStep());

    const run_step = b.step("run", "Run the substrate viewer");
    run_step.dependOn(&run_cmd.step);
}

