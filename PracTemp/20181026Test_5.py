# 함수

def add_txt(arg1, arg2):
    print(arg1, arg2)

param1 = '대~한민국~'
param2 = '짝짝~짝~ 짝.짝!!'
add_txt(param1, param2)

# 함수 호출1,  No Return Function
def sayHello():
    print('Hi, Guys !!')

sayHello()    # print(sayHello())

# 함수 호출2
def exchangeUSDtoKRW(dollar):
    won = dollar * 1065
    return won

usd = 2000
krw = exchangeUSDtoKRW(usd)
print('환전한 금액은 %d 원 입니다.'%(krw))

# 인세를 계산하는 함수
def calc_royalty(price, sales, per):
    rate = per / 100
    royalty = int(price * sales * rate)
    return royalty

i = input("책의 정가는？")      # 사용자가 정보를 입력한다
price = int(i)

i = input("발행 부수는？")
sales = int(i)

i = input("인세율(퍼센트)은？")
per = float(i)

v = calc_royalty(price, sales, per)    # 결과 표시
print("인세는 ", v, "원입니다.")