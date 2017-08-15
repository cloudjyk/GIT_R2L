#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO
from io import BytesIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())
f=StringIO('hello\nmike\nI\nhate\nyou')
while True:
    c=f.readline()
    if c == '':
        break
    print(c.strip())

f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))