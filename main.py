# -*- coding: utf-8 -*-

' a test module '
__author__ = 'aoaoao'

import re

def name_of_email(addr):
    reg = re.compile(r'^\<*([\w\s]*)\>*([\s\w]*)@(\w+)\.org$')
    return reg.match(addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')