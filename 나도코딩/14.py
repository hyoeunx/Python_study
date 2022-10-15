# 문자열 포멧

python = '파이썬'
java = '자바'

print(python + java)
print(python + ' ' + java)
print(python, java)

print('{}, {}를 배우자'.format(python, java))
print('{1}, {0}를 배우자'.format(python, java))
print(f'{python}, {java}를 배우자')
