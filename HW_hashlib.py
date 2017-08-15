#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
def user_reg():
    userN = input('Plz input your user name:\n')
    userPW = input('Plz input your password\n')
    PW_ini = hashlib.md5()
    if userPW == '123456':
        PW_ini.update((userPW+'userN').encode('utf-8'))
    else:
        PW_ini.update(userPW.encode('utf-8'))
    PW_ini_md5=PW_ini.hexdigest()
    # print('origin PW:',PW_ini_md5)
    return [userN,PW_ini_md5]

def user_login(*args):
    # print(args)
    userN = args[0]
    PW_ini_md5 = args[1]
    print('Log in:')
    userN_login = input('Plz input your username:')
    while not (userN == userN_login):
        userN_login = input('Wrong user name\nPlz input your username again:')
    PW_input = input('Plz input your password:')
    PW_login = hashlib.md5()
    if PW_input == '123456':
        PW_login.update((PW_input+'userN').encode('utf-8'))
    else:
        PW_login.update(PW_input.encode('utf-8'))
    PW_login_md5 = PW_login.hexdigest()
    # print('origin PW:',PW_ini_md5)
    # print('login PW:',PW_login_md5)
    if PW_ini_md5 == PW_login_md5:
        print('Welcome %s' % userN)
    else:
        print('Wrong password!')
        # print(args)
        user_login(args[0],args[1])

if __name__ == '__main__':
    user_data = user_reg()
    # print(user_data)
    user_login(user_data[0],user_data[1])