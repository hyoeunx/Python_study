# 사용자 입력

name = input('이름 입력 : ')


num = input('학번 입력 : ')

print(f'{name}입니다')
print(f'학번은 {num}')

if(num.startswith('1')):
    print('1학년입니다')
elif(num.startwith('2')):
    print('2학년입니다')