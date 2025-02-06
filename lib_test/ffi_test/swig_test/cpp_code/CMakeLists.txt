cmake_minimum_required(VERSION 3.7)
set(project_name python_swig_cpp)
set(CMAKE_CXX_STANDARD 14)

project(${project_name})

#设置版本号
set(VERSION_MAJOR 1.2)
set(VERSION_MINOR 0)

#log 选项
# 默认不使用boost, 减少依赖
#add_definitions(-DLOG_BOOST)

# 设置conan 参数
#set(CONAN_ARGS "${CONAN_ARGS} ")
message("CONAN_ARGS: ${CONAN_ARGS}")
option(IGNORE_CONAN "ignore conan load" on)

# 设置源码根目录(包含cmake的文件夹将被解析为一个编译target)
set(SRC_DIR_ROOT ${CMAKE_SOURCE_DIR}/src)
# 设置配目录(运行时拷贝)
set(CONFIG_DIR ${CMAKE_SOURCE_DIR}/data)
# 设置 boostStrap 文件夹名
set(BOOTSTRAP_DIR ${CMAKE_SOURCE_DIR}/cpp_bootstrap)

# 环境
include(cpp_bootstrap/common/CMake/FuncDefs.cmake)
set(DEFAULT_BIN_DIR ${CMAKE_BINARY_DIR}/bin)
SetBinDir(${DEFAULT_BIN_DIR})
set(SWIG_OUT_BASE ${CMAKE_SOURCE_DIR}/../cpp)

add_definitions(-DSWIG_PYTHON_INTERPRETER_NO_DEBUG)
FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})

find_package(PythonLibs REQUIRED COMPONENTS Interpreter Development)
message("${PYTHONLIBS_FOUND}")
message("${PYTHON_LIBRARIES}")
message("${PYTHON_INCLUDE_DIRS}")
message("${PYTHONLIBS_VERSION_STRING}")
message("${PYTHON_LIBRARY}")
message("${PYTHON_INCLUDE_DIR}")

include_directories(${PYTHON_INCLUDE_DIRS})


# 开始加载
include(cpp_bootstrap/BasicCmake.cmake)
AddAllSubDir()