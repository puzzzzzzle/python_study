#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : puzzzzzzle
# @Content : 通过.号访问的Storage

class Storage(dict):
    """
    let dict support d.var=1, d.var, del d.var

    test merge from dict:
    >>> data = {"var1":11,"var2":22,"d1":{"var1":33}}
    >>> s1 = Storage(data)
    >>> print(s1)
    <Storage {'var1': 11, 'var2': 22, 'd1': <Storage {'var1': 33}>}>

    test copy:
    >>> assert isinstance(s1,Storage)
    >>> assert isinstance(s1.d1,Storage)
    >>> import copy
    >>> s2 = copy.copy(s1)
    >>> print(s2)
    <Storage {'var1': 11, 'var2': 22, 'd1': <Storage {'var1': 33}>}>

    only copy s1, s1.d1 not copy:
    >>> assert id(s1)!=id(s2)
    >>> assert id(s1.d1)==id(s2.d1)

    by use deepcopy, s1.d1 also be copyed:
    >>> import copy
    >>> s3 = copy.deepcopy(s1)
    >>> assert id(s1)!=id(s3)
    >>> assert id(s1.d1)!=id(s3.d1)
    """

    def __init__(self, *args, **kwargs):
        super(Storage, self).__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = Storage(value)

    def __getattr__(self, attribute):
        try:
            return self[attribute]
        except KeyError:
            raise AttributeError(f"No such attribute: {attribute}")

    def __setattr__(self, attribute, value):
        self[attribute] = value

    def __delattr__(self, attribute):
        if attribute in self:
            del self[attribute]
        else:
            raise AttributeError(f"No such attribute: {attribute}")

    def __repr__(self):
        """
        str(obj)的显示内容
        :return:
        """
        return '<Storage ' + dict.__repr__(self) + '>'

    def _deepcopy(self):
        import copy
        new_dict = Storage()
        for key, value in self.items():
            if isinstance(value, Storage):
                new_dict[key] = value._deepcopy()
            else:
                new_dict[key] = copy.deepcopy(value)
        return new_dict

    def __deepcopy__(self, memodict):
        return self._deepcopy()


if __name__ == '__main__':
    import doctest

    doctest.testmod()
