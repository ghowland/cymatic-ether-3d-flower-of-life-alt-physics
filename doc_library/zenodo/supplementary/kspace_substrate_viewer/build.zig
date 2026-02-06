const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const exe = b.addExecutable(.{
        .name = "substrate_viewer",
        .root_module = b.createModule(.{
            .root_source_file = b.path("src/kspace_substrate_viewer.zig"),
            .target = target,
            .optimize = optimize,
        }),
    });

    // Allow turning off the console with: -Dsubsystem=Windows
    const subsystem = b.option(std.Target.SubSystem, "subsystem", "Set the subsystem (Console or Windows)") orelse .Console;
    exe.subsystem = subsystem;

    const raylib_dep = b.dependency("raylib_zig", .{
        .target = target,
        .optimize = optimize,
    });

    const raylib = raylib_dep.module("raylib"); // main raylib module
    const raygui = raylib_dep.module("raygui"); // raygui module
    const raylib_artifact = raylib_dep.artifact("raylib"); // raylib C library

    // Link raylib
    exe.linkLibrary(raylib_artifact);
    exe.root_module.addImport("raylib", raylib);
    exe.root_module.addImport("raygui", raygui);

    exe.linkLibC();


    const run_cmd = b.addRunArtifact(exe);
    run_cmd.step.dependOn(b.getInstallStep());

    // Run step
    const run_step = b.step("run", "Run the substrate viewer");
    run_step.dependOn(&run_cmd.step);


    b.installArtifact(exe);
}

