# 문자열 처리
from unicodedata import name


a = '심효은'
b = '1311'

school = a + b
school += '409호'
print(school)   #심효은1311409호

# 문자열 이외 다른 자료형에서도 사용 가능
num = 3

num += 2    #5
num -= 1    #4
num *= 2    #8
num /=4     #2.0

# 길이(length)
name = '심효은이다'
print(len(name))    #5

# 여러 줄 문자
nct = '''김정우
정우
엔시티127'''
print(nct)
#김정우
#정우
#엔시티127