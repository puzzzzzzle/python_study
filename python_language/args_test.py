# 在参数中:
# * 将后面的参数当做一个tuple
# ** 将后面的参数当做一个map

# 才传参中:
# * 将这个tuple解开, 而非当做单个参数传递
# ** 将这个map解开, 而非当做单个参数传递

# 简单讲: 函数申明处表示要打包后传入, 调用的地方表示这个tuple/dict要解包后传递

def arg_raw(var, *args, **kwargs):
    print(f"var {var} *args {args} **kwargs{kwargs} ")


# var 1 *args (3.14, 'ss') **kwargs{'aa': 1, 'bb': 2}
arg_raw(1, 3.14, "ss", aa=1, bb=2)

a1 = (3.14, "ss")
a2 = {"aa": 55, "bb": 66}

# var 2 *args ((3.14, 'ss'), {'aa': 55, 'bb': 66}) **kwargs{}
arg_raw(2, a1, a2)
# var 3 *args (3.14, 'ss', {'aa': 55, 'bb': 66}) **kwargs{}
arg_raw(3, *a1, a2)
# var 4 *args (3.14, 'ss', 'aa', 'bb') **kwargs{}
arg_raw(4, *a1, *a2)
# var 5 *args (3.14, 'ss') **kwargs{'aa': 55, 'bb': 66}
arg_raw(5, *a1, **a2)
