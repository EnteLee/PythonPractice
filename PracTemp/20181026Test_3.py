#

# s = input('영어 대소문자로 이루어진 문장을 입력하세요 \n')
# print('모두 대문자로 출력\n' + s.upper())
# print('모두 소문자로 출력\n' + s.lower())
#
# new_s = str()
#
# for c in s:
#     if c.islower():
#         new_s += c.upper()
#     else:
#         new_s += c.lower()
#
# print("대소문자 바꿔서 출력 \n"+new_s)
# print("대소문자 바꿔서 출력 \n"+s.swapcase(s))




s= input("영어 문장을 입력하세요")
new_s = str()
for x in range(len(s)-1,-1,-1):
    new_s += s[x]
print(new_s)
print(s[::-1])


