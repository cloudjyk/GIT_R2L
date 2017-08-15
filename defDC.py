# -*- coding: utf-8 -*-
import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kw):
#         print('begin call %s():' % func.__name__)
#         # return func(*args,**kw)
#         # return func()
#         func(*args,**kw)
#         print('end call %s():' % func.__name__)
#     return wrapper

# triple
def log(text):
    def decorator(func = text):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if not func == text:
                print('%s begin call %s():' % (text,func.__name__))
                func(*args,**kw)
                print('end call %s():' % func.__name__)
            else:
                print('begin call %s():' % (func.__name__))
                func(*args,**kw)
                print('end call %s():' % func.__name__)
        return wrapper
    return decorator
# @log('excute')
@log('excute')
def now():
    print('2017-6-11')
now()
print('fucname:%s\n' % now.__name__)
@log
def now():
    print('2017-6-11')
now()()
print('fucname:%s' % now.__name__)
# log(now)
# now = log('excute')(now)
# now()
# xx = log(now)
# xx()()()