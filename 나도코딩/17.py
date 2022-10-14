# 리스트2

list = ['심', '효', '은']
list2 = ['부산소마고', '1311']

print(list[0:2])    #['심', '효']
print('심' in list) #True
print(len(list))    #3
list[0] = '민'      #값 수정
list.remove('심')   #값 삭제
list.extend(list2)  #리스트 확장
print(list) #['심', '효', '은', '부산소마고', '1311']
