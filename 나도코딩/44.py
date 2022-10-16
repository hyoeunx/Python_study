# 전역변수

message = '전역변수'


def no_secret():
    # message = '지역변수'
    # print(message)  #지역변수
    global message
    message = '이건 전역변수'
    print(message)
    
print(message)  #전역변수
no_secret() #지역변수
print(message)  #이건 전역변수


x = 3
def add():
    x = 6
    x += 3
add()
print(x)    #3