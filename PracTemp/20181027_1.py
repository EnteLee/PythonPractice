# 함수 계속
# Arbitrary Arguments, 가변 인자 리스트 활용
def introduceMyFamily(my_name, *family_names, **family_info):
    print('안녕하세요, 저는 %s 입니다.' % (my_name))
    print('-' * 35)
    print('제 가족들의 이름은 아래와 같아요. ')

    for name in family_names:
        print('* %s ' % (name), end='\t')
    else:
        print()
    print('-' * 35)

    for key in family_info.keys():
        print('- %s : %s ' % (key, family_info[key]))


introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
                  주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')


#unpacking
def add(a, b):
    return a + b

data = (10, 20)    # tuple
#print(add(data))
print(add(*data))  # unpacking

def introduce(name, greeting):
    return "{name}님, {greeting}".format(
        name=name,
        greeting=greeting,
    )

introduce_dict = {
    "name" : "김진수",
    "greeting" : "안녕하세요",
}
print(introduce(**introduce_dict))


def my_function():
    """ 아무것도 하지 않지만, 문서만 기술한 함수

    본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다.
    """
    pass

print(my_function.__doc__)

def introduce_your_family(name, *family_names, **family_info):
    '''
    가족을 소개하는 함수입니다.
    Args:
        name: 자기이름 입력하기
        *family_names: 가족이름 입력하기
        **family_info: 가족소개하기

    Returns: 없습니다.
    '''
    pass