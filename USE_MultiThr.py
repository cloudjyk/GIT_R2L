#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time,threading
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n=0
#     while n<5:
#         n+=1
#         print('thread %s >>> %s' %(threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s is endded.' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s is endded.' % threading.current_thread().name)


balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0:
    # print('thread %s is running...' % threading.current_thread().name)
    global balance
    balance = balance + n
    balance = balance - n
    # print('thread %s is endded.' % threading.current_thread().name)

def run_thread(n):
    # print('thread %s is running...' % threading.current_thread().name)
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

    # print('thread %s is endded.' % threading.current_thread().name)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
print('thread %s is running...' % threading.current_thread().name)
t1.start()
t2.start()
t1.join()
t2.join()
print('thread %s is endded.' % threading.current_thread().name)
print(balance)