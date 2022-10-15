# 자료형 변환

# 튜플 리스트(튜플 값 추가)
my_tuple = ('소마고', '심효은')
my_list = list(my_tuple)   #튜플을 리스트로 변환
my_list.append('1311')
my_tuple = tuple(my_list)   #리스트를 튜플로 변환

# 리스트 세트(중복 값 제거)
my_list = ['소마고', '심효은', '심효은']
my_set = set(my_list)     #리스트를 세트로 변환(중복값 제거)
my_list = list(my_set)    #세트를 리스트로 변환
print(my_list)           #['소마고', '심효은']

# 리스트 딕셔너리(순서 중요, 중복 값 제거)
my_list = ['소마고', '심효은', '심효은']
my_dic = dict.fromkeys(my_list) #리스트를 딕셔너리로 변환(중복값 제거)
print(my_dic)   #{'소마고': None, '심효은': None}
my_list = list(my_dic)  #딕셔너리를 리스트로 변경