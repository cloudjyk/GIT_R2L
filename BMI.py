# -*- coding: utf-8 -*-

#height = 1.75
#weight = 80.5
height=input('Your height is(cm) ')
weight=input('Your weight is(kg) ')
height=int(height)/100
weight=int(weight)
BMI=weight/height**2
print('Your BMI is %f' % BMI)
if BMI<18.5:
    print('Too light')
elif 18.5<=BMI<25:
    print('Normal')
elif 25<=BMI<28:
    print('Overweight')
elif 28<=BMI<32:
    print('Fat')
else:
    print('Too fat')