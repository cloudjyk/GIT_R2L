#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
Uin=input('Pls input you Email address...\n')
if re.match(r'^(\w.*)@([0-9a-zA-Z]{1,100})\.([com,cn,net]{1,3})$',Uin):
    print('Register OK\nYour username is %s' % Uin)
    m=re.match(r'^(\w.*)@([0-9a-zA-Z]{1,100})\.([com,cn,net]{1,3})$',Uin)
    print(m.group(0)+'\n'+m.group(1)+'\n'+m.group(2)+'\n'+m.group(3))
else:
    print('Error!Wrong Email address!')
# if re.match(r'^[0-9]{3}\-[0-9]{5}',Uin):
#     print('Register OK\nYour phone number is %s' % Uin)
# else:
#     print('Error!Wrong Email address!')

# a=r'w\dw\a\31\n'
# print(a)
# a='w.-dwa\\31\n'
# print(a)