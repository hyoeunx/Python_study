# 세트 2

set = {'심효은', '부산소마고', '혜화여중'}

set.add('용호초')   #추가
print(set)  #{'심효은', '부산소마고', '혜화여중', '용호초'}

set.remove('용호초')    #삭제
print(set)  #{'심효은', '부산소마고', '혜화여중'}

set.clear() #모든 값 삭제
print(set)  #set()

del set #완전 삭제
print(set)  #세트 자체 삭제