number = 520
t = 0
guess = int(input('请输入一个整数：'))     #等待输入整数
while t != 1:
    #guess = int(guess)
    if guess == number:
        #print('恭喜，你猜对了。')    # 新块从这里开始
        print('Yes, I love you too !!')    # 新块在这里结束
        t=1
    elif guess < number:
        print('A little samller!')    # 另一个块
        guess = int(input('请再输入一个整数：'))     #等待输入整数
    else:
        print('Too big!')
        guess = int(input('请再输入一个整数：'))     #等待输入整数
print('Thank you!')
# if语句执行完后，最后的语句总是被执行