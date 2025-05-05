import gc


def triger_garbage():
    # 你的代码，这里制造一个循环引用
    class A:
        pass

    a = A()
    b = A()
    a.b = b
    b.a = a

    del a
    del b


def test_gc_collect():
    # 开启调试
    gc.set_debug(gc.DEBUG_SAVEALL)

    # 产生循环引用
    triger_garbage()

    # 手动触发垃圾回收
    unreachable = gc.collect()
    print(f"不可达对象数量: {unreachable}")

    # 打印被回收的对象
    for obj in gc.garbage:
        print("被回收的对象:", obj, type(obj))


def test_gc_leak():
    gc.set_debug(gc.DEBUG_LEAK)
    # 产生循环引用
    triger_garbage()


def test_gc_status():
    gc.set_debug(gc.DEBUG_STATS)
    # 产生循环引用
    triger_garbage()
    print("*"*30)
    gc.collect()
    print("*"*30)

if __name__ == '__main__':
    gc.collect()
    # test_gc_collect()
    # test_gc_leak()
    test_gc_status()
    pass