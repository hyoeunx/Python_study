# 문자열 메소드 2

s = '부산소마고'
a = '..부산소마고..'

#'부산'으로 시작하는지
print(s.startswith('부산')) #True

#'예고'로 끝나는지
print(s.endswith('예고'))   #False

#'.'앞뒤로 제거

print(a.strip('.'))  #부산소마고
# 만약 괄호 속에 아무것도 넣지 않으면 공백 제거

#소마고를 예고로
print(s.replace('소마고', '예고'))  #부산예고

#'소마고' 위치
print(s.find('소마고')) #2

#다른 문자들 사이에 가운데로
print(s.center(9, '-'))
#print(s.center(문자열길이, '문자'))

