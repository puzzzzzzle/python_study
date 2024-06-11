import sys
from pathlib import Path

sys.path.append(f"{Path(__file__).parent.absolute()}")
print(sys.path)

import cffi_test_lib

# 调用C函数
result = cffi_test_lib.lib.call_c(10)
print(f"result is {result}")