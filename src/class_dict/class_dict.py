class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.
        定义一个容器，可以使用obj.foo的方式来访问其间的数据，实际继承自字典dict
        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'

    """

    def __getattr__(self, key):
        """
        通过"."读取某个key的值
        :param key:
        :return:
        """
        return self[key]

    def __setattr__(self, key, value):
        """
        通过"."设置某个key的值
        :param key:
        :param value:
        :return:
        """
        self[key] = value

    def __delattr__(self, key):
        """
        删除属性
        :param key:
        :return:
        """
        if key in self:
            del self[key]

    def __repr__(self):
        """
        str(obj)的显示内容
        :return:
        """
        return '<Storage ' + dict.__repr__(self) + '>'

class Base:
    def name(self):
        return self.__class__.__name__
    def id(self):
        return 0
class Stub(Base):

    def id(self):
        return 1

if __name__ == '__main__':
    b = Base()
    s = Stub()
    print(f"{b.name()}  {b.id()}")
    print(f"{s.name()}  {s.id()}")

    d = Storage()
    d.a = "aha"
    print(f"d.a {d.a}  d['a']: {d['a']}")
