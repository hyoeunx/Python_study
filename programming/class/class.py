class human:    # class 이름 정의
    def __init__(self, height, age):    # class가 처음 호출될 때 method
        self.height=height  # class 변수
        self.age=age
        
    def how_old(self):  # class 메소드
        print(self.age, "살 입니다.")
    
    def how_tall(self):
        print(self.height, "cm 입니다.")

hyoeun = human(162, 17)
jw = human(180, 18)

hyoeun.how_old()
human.how_old(jw)

hyoeun.how_tall()
human.how_tall(jw)

print(hyoeun.height)