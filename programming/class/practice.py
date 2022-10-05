class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다. ".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wrait2 = Unit("빼앗은 레이스", 80, 5)
wrait2.clocking = True

if wrait2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wrait2.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]"
        .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다"
        .format(self.name, damage))

        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다."
        .format(self.name, self.hp))
        
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))