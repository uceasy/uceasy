def make_dist():
    return default_python_distribution()

def make_exe(dist):
    config = PythonInterpreterConfig(
        run_eval="from uceasy.console import cli; cli()",
        raw_allocator="system",
    )
    exe = dist.to_python_executable(
            name="uceasy",
            config=config,
            extension_module_filter="all",
            include_sources=True,
            include_resources=False,
            include_test=False,
    )
    exe.add_python_resources(dist.pip_install(["--pre", "uceasy"]))

    return exe


register_target("dist", make_dist)
register_target("exe", make_exe, depends=["dist"], default=True)
resolve_targets()




PYOXIDIZER_VERSION = "0.6.0"
PYOXIDIZER_COMMIT = "UNKNOWN"
