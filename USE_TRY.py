#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# import logging
# try:
#     print('Start...')
#     r=2/1
#     print('Result:',r)
# except ZeroDivisionError as e:
#     # raise
#     logging.exception(e)
#     print('Error:')
# else:
#     print('pass')
# finally:
#     print('Finally...')

# try:
#     print('try...')
#     r = 10 / int('10')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')



# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)

# main()
# print('END')

# class FooError(ValueError):
#     pass
# def main(n):
#     a=int(n)
#     if a==0:
#         raise FooError('FooError occured:%s' % n)
#     print(10/a)
# main('2')
# main('0')

# def foo(s):
#     n = int(s)
#     if n==0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n

# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         print('ValueError!')
#         raise

# bar()
# print('END')


# try:
#     10 / 0
# except ZeroDivisionError:
#     raise ValueError('input error!')


a=0
try:
    10/a
except ZeroDivisionError as e:
    print('Error:%s',e)
else:
    pass
finally:
    pass
# c=10/a
print('END')