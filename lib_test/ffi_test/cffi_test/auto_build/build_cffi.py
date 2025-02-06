# 使用 cffi 编译, 而非makefile提前编译
from cffi import FFI

ffi = FFI()

# 描述C函数和数据类型
ffi.cdef("""
    int call_c(int val);
""")

# 加载共享库
ffi.set_source("cffi_test_lib",
               """
               #include "../lib.h"
               """,
               libraries=[],
               sources=["../lib.c"])

if __name__ == "__main__":
    ffi.compile()