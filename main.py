# -*- coding: utf-8 -*-

' a test module '
__author__ = 'aoaoao'

class Screen(object):
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, x):
        if not isinstance(x, int):
            raise TypeError('sdf')
        self._width = x
    @property
    def height(self):
        return self._height
    
    @width.setter
    def height(self, x):
        if not isinstance(x, int):
            raise TypeError('sdf')
        self._height = x
    @property
    def resolution(self):
        return self._width * self._height
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')