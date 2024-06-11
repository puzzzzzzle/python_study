import consts

loggger = consts.get_logger(__name__)

num = 42


def test_func_1():
    # compile error
    # loggger.info(num)
    num = 80
    loggger.info(num)


def test_func_2():
    global num
    loggger.info(num)
    num = 80
    loggger.info(num)


def test_4():
    aha = 70

    def test_3():
        loggger.info(aha)

    def test_4():
        # compile error
        # loggger.info(aha)
        nonlocal aha
        loggger.info(aha)
        aha = 400
        loggger.info(aha)

    test_4()
    test_3()


if __name__ == '__main__':
    test_func_2()

    loggger.info(num)
    test_4()
