# -*- coding: utf-8 -*-

class Array(object):
    def __init__(self,size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        #魔术方法，通过它实现括号访问
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self,value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1