cmake_minimum_required(VERSION 3.15)
project(cpp_code)

set(CMAKE_CXX_STANDARD 14)

function(UnixFlag)
    message("cmake build type : ${CMAKE_BUILD_TYPE}")
    set(CMAKE_CXX_FLAGS "-fPIC ${CMAKE_CXX_FLAGS}")
    if ("${CMAKE_BUILD_TYPE}" STREQUAL "Debug")
        set(CMAKE_CXX_FLAGS "-Wall -O0  -g -ggdb ${CMAKE_CXX_FLAGS}")
    elseif ("${CMAKE_BUILD_TYPE}}" STREQUAL "Release")
        set(CAKE_CXX_FLAGS "-O3 -Wall ${CMAKE_CXX_FLAGS}")
    else ()
        message("unknow type:${CMAKE_BUILD_TYPE}")
    endif ()
    message("cmake cxx build flags:${CMAKE_CXX_FLAGS}\n")
endfunction()

if (WIN32)
    MESSAGE(STATUS "Now is windows")
elseif (APPLE)
    MESSAGE(STATUS "Now is Apple systens.")
    UnixFlag()
elseif (UNIX)
    MESSAGE(STATUS "Now is UNIX-like OS's.")
    UnixFlag()
endif ()


add_definitions(-DSWIG_PYTHON_INTERPRETER_NO_DEBUG)
FIND_PACKAGE(SWIG REQUIRED)
INCLUDE(${SWIG_USE_FILE})

find_package(Python REQUIRED COMPONENTS Interpreter Development)
message("inc:\t${Python_INCLUDE_DIRS} \tlibs:\t${Python_LIBRARIES} \tlinked:\t${Python_LIBRARY} \t${Python_LIBRARY_DIRS}")
include_directories(${Python_INCLUDE_DIRS})
link_directories(${Python_LIBRARY_DIRS})
#link_libraries(${Python_LIBRARY})


SET(CMAKE_SWIG_FLAGS "")


function(AddDir target)
    #    execute_process(
    #            COMMAND_ECHO STDOUT
    #            COMMAND python3 ${CMAKE_SOURCE_DIR}/gen_code.py ${target}
    #            OUTPUT_VARIABLE execute_process_o
    #            ERROR_QUIET
    #    )
    #    message("add_custom_command: ${execute_process_o}\n")
    set(src_dir ${CMAKE_SOURCE_DIR}/cpps/${target})
    set(gen_dir ${CMAKE_SOURCE_DIR}/cpp_gen/${target})
    set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${gen_dir})
    set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${gen_dir})
    set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${gen_dir})

    include_directories(${src_dir})
    aux_source_directory(${src_dir} cpps)

    # 可执行文件
    if (EXISTS "${CMAKE_SOURCE_DIR}/cpps/${target}/main.cpp")
        add_executable(${target}_exe ${cpps} ${src_dir}/main.cpp)
    endif ()
    #通用动态链接库
    aux_source_directory(${gen_dir} cpp_gen)
    add_library(_${target} SHARED ${cpps} ${cpp_gen})

    # swig 动态库
    set(swig_i ${src_dir}/${target}.i)
    SET_SOURCE_FILES_PROPERTIES(${swig_i} PROPERTIES CPLUSPLUS ON)
    #    SET_SOURCE_FILES_PROPERTIES(${swig_i} PROPERTIES SWIG_FLAGS "-includeall")
    SET_SOURCE_FILES_PROPERTIES(${swig_i} PROPERTIES SWIG_FLAGS "-py3")

    SWIG_ADD_LIBRARY(${target}
            TYPE SHARED
            LANGUAGE python
            OUTPUT_DIR ${gen_dir}
            OUTFILE_DIR ${gen_dir}
            SOURCES ${swig_i} ${cpps})
    SWIG_LINK_LIBRARIES(${target} ${Python_LIBRARY})
endfunction()

AddDir(word)
AddDir(word_1)
