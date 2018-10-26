# 숫자값 N을 입력받아, 1~N 까지의 Sum 과 Factorial 구하기
# 1. 입력값에 대한 Validation 체크
# 2. 숫자값이 아닌경우 재입력 유도
# 3. Sum과 Factorial 결과값을 list에 저장 후 한꺼번에 출력

while True :
    i = input("숫자를 입력해주세요.1~100")
    j=list(i)
    x=0
    y=0
    sum=0
    fac=1
    fac_list= []

    while x < len(j):
        for y in range(0, 10, 1):
            check = j[x] != str(y)
            if check == False:
                break
            else:
                pass
        x+=1
        if check == True:
            print("입력값이 숫자가 아닙니다")
            break
        else:
            pass
    if check:
          pass
    else:
         if 0 <= int(i) <= 100:
             break
         else :
              x= len(j)
              print("범위를 확인하세요.1~100")


i = int(i)
print(i, "까지의 합계 및 팩토리얼 테이블 구하기")

for w in range(1,i+1,1):
    sum = sum+w

print(i, "까지의 합계는", sum)
print("아래는 팩토리얼 테이블")
w=0
for w in range(1, i+1,1):
    fac_list.append(fac)
    fac= fac*w
#    print(w,"! = ",fac)
w=0
for w in range(1,i+1,1):
    print(w,"! = ",fac_list[w-1])


#
# while True:
#     key_in = input("숫자값을 입력하세요. 1~100")
#     is_num = True
#     check_num = list('0123456789')
#     for char in list(key_in):
#         print(char)
#         is_num = is_num * int(char in check_num)
#         if not is_num:
#             break
#     if check_num :
#         key_in = int(key_in)
#         print("입력한 값은 %d 입니다" %key_in)
#         break
#     else :
#         print("입력한 값은 숫자가 아닙니다.")
# sum = []
# fac = []
#
# for num in range(key_in):
#     sum += num
#     gop += num
#     if gop ==0
#         gg+1
#     sum.speed(sum
#               factorial.apppenfm)
#
# print(sum)
# print(fac)
# print()