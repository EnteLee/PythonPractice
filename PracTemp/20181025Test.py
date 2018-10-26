"""
sistar_members = ['효린', '소유']
print('씨스타 \t:', sistar_members)

sistar_members.append('다솜')
print('append \t:', sistar_members)

sistar_members.insert(1, '보라')
print('insert \t:', sistar_members)

sistar_members.remove('소유')
print('remove \t:', sistar_members)

pickup = sistar_members.pop(0)
print('pop   \t:', sistar_members, end=' ---> ')
print(pickup)


rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
print('\n무지개색깔 \t :', rainbow)

result = rainbow[2:5]
print('rainbow[2:5] :', result)

result = rainbow[:3]
print('rainbow[ :3] :', result)

result = rainbow[:]
print('rainbow[ : ] :', result)

result = rainbow[::2]
print('rainbow[::2] :', result)

result = rainbow[-3:]
print('rainbow[-3:] :', result)

result = rainbow[::-1]
print('rainbow[::-1]:', result)
"""
"""
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
print('태양계 :', solarsys)

# 리스트에서 특정 요소의 위치 구하기(index)
planet = '지구'
pos = solarsys.index(planet)
print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
pos = solarsys.index(planet, 5)
print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))

# 리스트에서 특정 위치의 요소를 변경하기
solarsys.pop(-1)
print('태양계 :', solarsys)

planet = '화성'
pos = solarsys.index(planet)
solarsys [pos] = 'Mars'
print('태양계 :', solarsys)

# 리스트에서 특정 구간에 있는 요소 추출하기
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
rock_planets = solarsys[1:5]
gas_planets  = solarsys[5: ]

print('암석형 행성: ', end=''); print(rock_planets);
print('가스형 행성: ', end=''); print(gas_planets);
print('암석 : ', rock_planets)
print('가스 : ', gas_planets)

# 리스트의 특정 위치에 요소 삽입하기(insert)
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print('태양계 :', solarsys)
"""
"""
city = [
    ['서울',  '도쿄',  '베이징'],
    ['런던',  '파리',  '로마'  ],
    ['워싱턴','시카고','잭슨빌']
]

print('city      :', city)
print('city[0]   :', city[0])
print('city[1]   :', city[1])
print('city[-1]  :', city[-1])
print('city[0][0]:', city[0][0])
print('city[0][1]:', city[0][1])
print('city[0][2]:', city[0][2])
print('city[1][1]:', city[1][1])
print('city[2][0]:', city[2][0])
"""
"""

#튜플 생성(튜플형, tuple type)
girl_group = ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')

print('girl_group    \t: ', girl_group)
print('girl_group[:2] \t: ', girl_group[:2])
print('girl_group[-2:] : ', girl_group[-2:])

girl_group = list(girl_group)
girl_group[2] = '블랙핑크'
girl_group = tuple(girl_group)
print('girl_group   \t: ', girl_group)

width  = 20
height = 30
area = width * height

print('너비 :', width);
print('높이 :', height);
print('넓이 :', area)


data   = (15, 50)
width, height = data
area = width * height


print('너비 :', width);
print('높이 :', height);
print('넓이 :', area)
"""

"""
lang = {'Java', 'Java', 'Python', 'C++', 'Python'}
print(lang)
print(type(lang))
print('Python'in lang)
print('Javascript'in lang)


a = set('abracadabra')
b = set('alacazam')

print('집합 a =', a);  print('집합 b =', b);
print('합집합, a | b =', a | b)
print('교집합, a & b =', a & b)
print('차집합, a - b =', a - b)
print('여집합, a ^ b =', a ^ b)


beast = ["lion", "tiger", "wolf", "tiger", "lion", "bear", "lion" ]
print('beast =', beast)

unique_beast = list(set(beast))
print('unique_beast =', unique_beast)
sorted_beast = sorted(unique_beast)
print("sorted_beast =", sorted_beast)
"""
"""
# 사전형 생성
bans = { '잎새반':'찬영이',
         '열매반':'예영이',
         '햇살반':'준영이',
         '열매반':'채영이', }

print(type(bans))
print('반의수 : ', len(bans))

# 읽기
print('잎새반 : ', bans['잎새반'])
print('열매반 : ', bans['열매반'])
print('햇살반 : ', bans['햇살반'])
print('bans 읽기 :', bans)

# 추가
bans['꽃잎반'] = '희영이'
print('bans 추가 :', bans)

# 변경
bans['잎새반'] = '서영이'
print('bans 변경 :', bans)

# 삭제
del bans['햇살반']
print('bans 삭제 :', bans)

"""