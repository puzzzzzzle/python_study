import logging
import collections

import json
import random
import consts

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
    for k, v in map1.items():
        show_val(k)
        show_val(v)


class Child(object):
    def __init__(self):
        self.var1 = 1
        self.var2 = "c"
        self.var3 = ["cc", 2, "cc"]


class ChildEncoder(json.JSONEncoder):
    def default(self, o):
        logging.info(f"type(self){type(self)}")
        logging.info(f"type(o){type(o)}")
        dic_o = o.__dict__
        # dic_o["arr4"] = [item for item in o.arr4]
        return dic_o


class Parent(object):
    def __init__(self):
        self.var1 = 1
        self.var2 = "s"
        self.arr3 = ["s", 2, "ss"]
        c1 = Child()
        c2 = Child()
        arr = [c1, c2]
        # self.arr4 = [json.dumps(item.__dict__) for item in arr]
        self.arr4 = arr


def dict_test():
    p = Parent()
    jstr = json.dumps(p, indent=4, cls=ChildEncoder)
    logging.info(jstr)
    load_json = json.loads(jstr)
    load_p = Parent()
    load_p.__dict__ = load_json
    logging.info(json.dumps(load_p, indent=4, cls=ChildEncoder))

    pass


def dict_speed_test():
    d = {}
    import datetime
    start = datetime.datetime.now()
    for i in range(1000000):
        d[random.random()] = i
    end = datetime.datetime.now()
    logging.info(end - start)


def named_test():
    Point3D = collections.namedtuple("Point3D", ["x", "y", "z"])
    p = Point3D(3, 4, 5)
    logging.info(p)


if __name__ == '__main__':
    named_test()
