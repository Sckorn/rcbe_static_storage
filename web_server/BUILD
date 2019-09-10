py_library(
    name = "www",
    srcs = glob(["src/www/*.py"]),
    imports = ["src"],
)

py_binary(
    name = "webserver",
    srcs = ["src/webserver.py"],
    deps = ["www"],
    python_version = "PY2",
)
