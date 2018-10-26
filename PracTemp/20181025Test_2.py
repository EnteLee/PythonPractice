"""
weight = float(input("체중은?"))
height = float(input("키는?"))

height = height /100
bmi = weight / (height * height)

result = ""
if bmi < 18.5 :
    result = "마름"
elif (18.5 <= bmi) and (bmi < 25) :
    result = "보통"
elif (25 <= bmi < 30) :
    result = "비만"
elif (bmi >= 30) :
    result = "고도비만"

print("bmi :", bmi)
print("결과 :", result)
"""

"""
year = int(input("올해 몇년?"))

is_leap = (year % 400 == 0) or ((year%100 !=0) and (year%4 == 0))

if is_leap :
    print("윤년 입니다.")
else :
    print("윤년이 아닙니다.")
"""
"""
import turtle
in_color = input("원의 색을 입력하세요.(R/G/B/etc)")
in_fill = input("원 내부 색을 채우시겠습니까 (Y/N)")

if in_color == 'R' :
    color = 'Red'
elif in_color == 'G' :
    color = 'Green'
elif in_color == 'B' :
    color = 'Blue'
else :
    color = 'Black'

turtle.begin_fill()
turtle.color(color)
turtle.pensize(10)
turtle.circle(100)

if in_fill == 'Y' :
    turtle.end_fill()
else :
    pass

turtle.done()
"""

#while 문
"""
sigmal_color = ''

while sigmal_color != 'blue' and sigmal_color != 'red':
    sigmal_color = input('색을 영문으로 입력하세요 (blue/red) : ')

    if sigmal_color == 'blue':
        print('신호등은 파란색 입니다. 길을 건너세요!!')
    elif sigmal_color == 'red':
        print('신호등은 빨간색 입니다. 기다리세요.')
    else:
        print('잘못된 색입니다. 다시 입력해 주세요!!')

print('프로그램을 종료합니다.')

"""
"""
num, sum = 1, 0

while True:
    sum += num
    if sum > 100:
        break
    else:
        num += 1
        print(sum)

print('num 값이 %d 일때 while문 탈출 !!' % num)
"""
"""
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
idx, sum = 0, 0

while idx < len(numbers):
    num = numbers[idx]
    print(num)
    sum += idx
    idx += 1

print('numbers의 합계는', sum, '입니다.')
"""




#for문
"""
result = list(range(10))
print('range(10)', result)

scope = [1,2,3,4,5]
for i in scope:
    print(i)
scope = list('abcde')
for i in scope:
    print(i)
"""
"""
scope = list(range(1, 100))

for num in scope:

    if num <= 10:
        if num % 2 == 0:
            pass                                        #pass 는 if 뒤에 아무것도 없으면 오류나서 사용. but 이상황에선 없어도 ㄱㅊ
            print(num, 'is even number.')
        else:
            continue                                     #continue 쓰면 아래 print는 절대 작동 안함.
            print(num, 'is odd number.')
    else:
        print(num, 'is bigger than ten')
        break                                           #break 썼으니 당연히 after break 실행 안됨.
        print('after break')

print('프로그램을 종료합니다.')
"""

"""
bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
num = 0

for member in bts_members:
    num += 1
    print('멤버%d ====> %s  \t(이름길이:%d)' % (num, member, len(member)))

size = len(bts_members)

for idx in range(size):
    print('멤버%d ====> %s  \t(이름길이:%d)' % (idx+1, bts_members[idx], len(bts_members[idx])))
"""
"""
for i in range(1, 10, 2):              #1~10까지 +2 인 느낌적인 느낌
    mark = "*" * i
    print(mark)

for i in range(1, 10, 2):
    mark = " " * int((10-i)/2) + "*" * i
    print(mark)
"""
"""
import turtle as t
num_circle = 10
radius = 150

t.bgcolor("blue")
t.color("yellow")
t.speed(0)

for _ in range(num_circle):
    t.circle(radius)
    t.left(360/num_circle)

t.done()
"""

import turtle as t

for _ in range(6) :
    t.forward(100)
    t.right(60)
t.left(120)
for _ in range(5) :
    for _ in range(7):
        t.forward(100)
        t.right(60)
    t.left(120)
t.done()

"""
import turtle as t
import math

#math.sqrt(a**2*2)

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(135)
t.forward(math.sqrt(100**2*2))
t.left(135)
t.forward(100)
t.left(135)
t.forward(math.sqrt(100**2*2))
t.right(135)
t.forward(100)
t.right(45)
t.forward(math.sqrt(100**2*2)/2)
t.right(90)
t.forward(math.sqrt(100**2*2)/2)

t.done()
"""
