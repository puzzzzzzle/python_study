#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : puzzzzzzle
# @Content : 通过.号访问的Storage

class Storage(dict):
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
