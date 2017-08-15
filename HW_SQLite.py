#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sqlite3
db_file = os.path.join(os.path.dirname(__file__),'test.db')
print(db_file)
if os.path.isfile(db_file):
    os.remove(db_file)

#initial data
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.execute(r"insert into user values ('A-004', 'Bill', 65)")
cursor.execute(r"insert into user values ('A-005', 'Mike', 77)")
cursor.execute(r"insert into user values ('A-006', 'Lucy', 71)")
cursor.execute(r"insert into user values ('A-007', 'Lily', 73)")
cursor.execute(r"insert into user values ('A-008', 'Lucifer', 75)")
cursor.execute(r"insert into user values ('A-009', 'Shelly', 82)")
cursor.execute(r"insert into user values ('A-0010', 'Jack', 91)")
cursor.execute(r"insert into user values ('A-0011', 'Micheal', 99)")
cursor.execute(r"insert into user values ('A-0012', 'Bob', 100)")
cursor.close()
conn.commit()
conn.close()
def rate_list(ori_list):
    rated_list = ori_list
    for i in range(len(ori_list)-1):
        for j in range(len(ori_list)-1-i):
            if rated_list[j][2] > rated_list[j+1][2]:
                temp = rated_list[j]
                rated_list[j] = rated_list[j+1]
                rated_list[j+1] = temp
    return rated_list
def get_score_in(low,high):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where score>=? and score<=?',(low,high))
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    print('Firstly We\'ve got:\n',values,'\n')
    if len(values) > 1:
        rated_list = rate_list(values)
        rated_name = []
        for i in range(len(rated_list)):
            rated_name.append(rated_list[i][1])
    else:
        rated_list = values
        rated_name = values[0][1]
    print('Then:\n',rated_list,'\n')
    print('At last we have:\n',rated_name,'\n')
    return rated_name
if __name__=='__main__':
    # assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
    # assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
    # assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
    get_score_in(80, 95)
    get_score_in(60, 80)
    get_score_in(60, 100)

