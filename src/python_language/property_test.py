class TestSimple(object):
    in_class = 'in_class_def'

    @property
    def pro_1(self):
        return self._pro_1

    @pro_1.setter
    def pro_1(self, value):
        self._pro_1 = value

    def __init__(self):
        self._pro_1 = "pro_def"
        self.self_p = "self_p_def"


if __name__ == '__main__':
    test1 = TestSimple()
    test2 = TestSimple()


    def print_class(p):
        print(
            f"ins.in_class:{p.in_class}      class.in_class:{TestSimple.in_class}        pro_1:{p.pro_1}        self_p:{p.self_p}")


    print_class(test1)
    print_class(test2)

    test1.in_class = "instence.in_class_new"
    test1.self_p = "self_p_new"
    test1.pro_1 = "pro_1_new"

    print_class(test1)
    print_class(test2)

    pass
