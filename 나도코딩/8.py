# 불리안

# 비교 연산자
from email.errors import FirstHeaderLineIsContinuationDefect


print(5>2) #True
print(5>=2) #True
print(5<2)  #False
print(5<=2) #False

#불리안 형 변환
bool()  #값이 있으면 True 없으면 Fasle
a = 'hello'
b = ' '
c = ''
print(bool(a))  #True
print(bool(b))  #True
print(bool(c))  #False
print(bool(None))   #Flase