import functools

def log_func_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'")
        result = func(*args, **kwargs)
        print(f"Finished function '{func.__name__}'")
        return result
    return wrapper

class MyClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def __getattribute__(self, name):
        attr = super().__getattribute__(name)
        if callable(attr):
            return log_func_call(attr)
        return attr

# 测试
my_obj = MyClass()
my_obj.increment()
my_obj.decrement()