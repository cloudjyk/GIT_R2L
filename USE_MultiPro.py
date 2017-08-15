#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1
# from multiprocessing import Process
# import os
# def run_pro(name):
#     print('Run child process %s (%s)' % (name,os.getpid()))
# if __name__=='__main__':
#     p=Process(target=run_pro,args=('test',))
#     # print(r'Let\'s start')
#     print('Let\'s start')
#     p.start()
#     p.join()
#     print('THE END')

# 2
# from multiprocessing import Pool
# import os, time, random
# def long_time_task(name):
#     print('Run task %s(%s)' % (name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end-start)))
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waiting for all the subprocesses to finish...')
#     p.close()
#     p.join()
#     print('All processes are done.')

# 3
# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code',r)

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
print(output.decode('gb2312'))
print('Exit code:', p.returncode)