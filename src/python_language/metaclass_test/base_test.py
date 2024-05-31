# class ClassA:
#   data = 1
# 最终等价于:
from collections import defaultdict

ClassA = type("ClassA", (object,), {"data": 1})
a = ClassA()
print(type(a))
print(a.data)


# type 其实也是一个内建对象, 只是实现了__CALL__ 方法
# 具体见 object.h _typeobject (PyTypeObject) 的struct
#     ternaryfunc tp_call; 即为call函数

# 我们自己实现一个实现了__CALL__的类, 也可以
# 简单起见, 继承自type, 再覆盖别的函数
class MyMetaClass(type):
    managed_classes = []

    def __init__(cls, name, bases, kwds):
        """
        这里cls 是 具体的子类的类型, 不是self, 比较特殊
        这里还在创建类型, 并不涉及具体子类对象的创建
        所以只要类型import了, 就会管理
        """
        print(f"will init {cls} {name} {bases} {kwds}")
        MyMetaClass.managed_classes.append(cls.__name__)
        super(MyMetaClass, cls).__init__(name, bases, kwds)


# 类对象中的 __new__ 只有在创建类时才会统计
class ManagedClassBase(metaclass=MyMetaClass):
    init_count = defaultdict(int)

    def __new__(cls):
        ManagedClassBase.init_count[cls.__name__] += 1
        return super().__new__(cls)

    pass


class ClassB(ManagedClassBase):
    pass


class ClassC(ManagedClassBase):
    pass


m = ManagedClassBase

b1 = ClassB()
b2 = ClassB()

print(f"MyMetaClass.managed_classes: {MyMetaClass.managed_classes}")
print(f"ManagedClassBase.init_count: {ManagedClassBase.init_count}")
