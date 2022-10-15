# 리스트 컴프리헨션

list = ['a-1', 'a-2', 'b-1', 'b-2']


a = []
for i in list:
    if i.startswith('a'):
        a.append(i)
print(a)    #['a-1', 'a-2']

# st가 b로 시작
b = [st for st in list if st.startswith('b')]
print(b)