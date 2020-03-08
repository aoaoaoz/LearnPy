# -*- coding: utf-8 -*-

' a test module '
__author__ = 'aoaoao'

from wsgiref.simple_server import make_server
from main import application

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()