# 提前编译的方式, 不用 build_cffi.py
LIB_NAME = cffi_test_lib

# 源文件
SRC = ../lib.c

# 检测操作系统
ifeq ($(OS),Windows_NT)
	TARGET = $(LIB_NAME).dll
else
	TARGET = $(LIB_NAME).so
endif

OBJ = $(SRC:.c=.o)

CC = gcc
CFLAGS = -Wall -g -fPIC
LDFLAGS = -shared
RM = rm -f

# 默认目标
all: $(TARGET)

# 链接目标文件
$(TARGET): $(OBJ)
	$(CC) $(OBJ) $(LDFLAGS) -o $(TARGET)

# 编译源文件
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# 清理目标文件和对象文件
clean:
	$(RM) $(OBJ) $(TARGET)

.PHONY: all clean