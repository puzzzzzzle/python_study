import platform

from cffi import FFI

ffi = FFI()

# 描述C函数和数据类型
ffi.cdef("""
    int call_c(int val);
""")

# 加载现有的共享库
if platform.system() == "Windows":
    # Windows
    lib = ffi.dlopen("./cffi_test_lib.dll")
else:
    # Linux
    lib = ffi.dlopen("./example.so")

# 调用C函数
result = lib.call_c(10)
print(f"result is {result}")
