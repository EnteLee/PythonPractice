# 파이썬 시작

"""
x=60
y=3
print(x+y)

string1 = "String Test 1"
string2 = 'String Test 2'
print(string1)
print(string2)

print(string1, string2)


coffee1_name = '카페라떼';  coffee1_val = 4000;
coffee2_name = '카푸치노';  coffee2_val = 4500;
coffee3_name = '마끼야또';  coffee3_val = 5000;
coffee_val = coffee1_val + coffee2_val + coffee3_val
print('손님, \n%s, %s, %s를 주문하셨습니다.' % (coffee1_name, coffee2_name, coffee3_name))
print('가격은 %d원 입니다.' % coffee_val)

name = input("what is your name?" )
print(name)


print ("몇잔 드릴까요?")
order = input()
order = coffee1_val * int(order)
print("가격은 %d원 입니다." %coffee_val)


coffee_val = 0
coffee1_val = 4000;
coffee2_val = 4500;
coffee3_val = 5000;

print("어떤 커피를 주문하시겠습니까? 1.카페라떼 2.카페모카, 3.마끼아또")
order = input()
if order==1:
    coffee_val = coffee_val1
elif order==2:
    coffee_val = coffee_val2
elif order==3:
    coffee_val = coffee_val3
else:
    print("잘못 주문하셨습니다.")

print ("몇잔 드릴까요?")
count = input()
result = coffee_val * int(count)
print("%d 원입니다." %result)

"""

# turtle exam
import turtle
import time
"""
input ('엔터를 치면 거북이를 소개합니다.^^')

turtle.shape('turtle')

turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward(30)
turtle.done()

input('엔터를 치면 파란색 굵은 원을 그립니다.')

turtle.right(30)
turtle.color("blue")
turtle.circle(100)

turtle.done()
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()