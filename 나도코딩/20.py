# 세트 1

# 여러 개 데이터 저장 가능
# 순서x, 중복x

A = {'심', '효', '은', '부산소마고'}
B = {'심', '효', '은', '혜화여중'}
print(A.intersection(B))    #교집합 #{'심', '효', '은'} #순서X
print(A.union(B))   #합집합 #{'심', '효', '은', '부산소마고', '혜화여중'}   #순서X
print(A.difference(B))  #차집합 #{'부산소마고'}
