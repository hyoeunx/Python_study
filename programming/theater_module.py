# 일반 가격
def price(people):
    print("{0} 명 가격은 {1} 원 입니다.".format(people, people * 10000))
    
# 조조할인 가격
def price_morning(people):
    print("{0} 명 조조할인 가격은 {1} 원 입니다.".format(people, people * 6000))
    
# 군인 할인 가격
def price_soldier(people):
    print("{0} 명 군인 할인 가격은 {1} 원 입니다.".format(people, people * 4000))


if __name__ = '__main__' :
    price(30) #모듈로 실행되면 15, 16 실행 X
    price_soldier(50)  #main일 경우 여기서부터 실행