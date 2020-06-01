import logging
import src


class DataTest(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"name is {self.name} ; self is {vars(self)} "

    def __str__(self):
        return f"DataTest name is {self.name}"


def show_val(val):
    logging.info(f"{val} : type is {type(val)}")


def show(con):
    logging.info(f"\n{con}")
    for item in con:
        logging.info(f"item is [{item}] type is {type(item)}")
        if type(item) == DataTest:
            logging.info(f"data show: {item.show()}")


def list_test():
    vec1 = [1, "ss", 4.4, DataTest, DataTest("data1")]
    show(vec1)
    tup1 = (1, "sss", 3.4)
    show(tup1)
    set1 = {1, 2, 3, 3, "3"}
    show(set1)
    map1 = {"key": 1, "val": "22"}
    show(map1)
    for k in map1:
        show_val(k)
        show_val(map1[k])
    for k,v in map1.items():
        show_val(k)
        show_val(v)


if __name__ == '__main__':
    list_test()
