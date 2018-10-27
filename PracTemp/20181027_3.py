# 클래스 정의 : X
"""
class MyClass:
    name = '희영'

    def sayHello():
        hello = "Hello, " + name + "\t It's Good day !"
        return hello


myClass = MyClass()
obj_name = myClass.name
obj_method = myClass.sayHello()

print('Object name   :', obj_name)
print('Object method :', obj_method)
"""

# 클래스 변수와 인스턴스 변수
# 변수의 선언 위치에 따라 달라지는 유효범위
class MyChildren:
    school = '대학교'       # 클래스변수 country 선언

    def __init__(self, name):     # 초기화 함수 재정의
        self.name   = name        # 인스턴스 변수 name 선언

    def go_to_school(self):
        print(self.name + '이는 ' + self.school + '에 다닙니다.')

# 객체 인스턴스화
myChild  = MyChildren('희영')
myChild1 = MyChildren('찬영')
myChild2 = MyChildren('준영')
myChild3 = MyChildren('채영')

myChild1.school = '고등학교'
myChild2.school = '중학교'
myChild3.school = '초등학교'

# 클래스함수 호출 (인스턴스 변수 name 출력)
myChild.go_to_school()
myChild1.go_to_school()
myChild2.go_to_school()
myChild3.go_to_school()


### class 변수로 지정시 객체에서 지정해도 메모리가 같은곳 을 가리켜서 값이 같아짐.
### init을 써서 선언하면 인스턴화 되서 독립적으로 객체마다 다르게 사용 가능.

# 클래스 변수
class Dog:
    tricks = []  # 클래스 변수 선언

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)  # 클래스 변수에 값 추가


dog1 = Dog('마음이')
dog2 = Dog('진돌이')

dog1.add_trick('구르기')
dog2.add_trick('두발로 서기')
dog2.add_trick('죽은척 하기')

print(dog1.name, ':', dog1.tricks)
print(dog2.name, ':', dog2.tricks)

# 인스턴스 변수
class Cat:
    def __init__(self, name):
        self.name = name
        self.tricks = []  # 인스턴스 변수 선언

    def add_trick(self, trick):
        self.tricks.append(trick)  # 인스턴스 변수에 값 추가


cat1 = Cat('하늘이')
cat2 = Cat('야옹이')

cat1.add_trick('구르기')
cat2.add_trick('두발로 서기')
cat2.add_trick('죽은척 하기')

print(cat1.name, ':', cat1.tricks)
print(cat2.name, ':', cat2.tricks)