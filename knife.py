# Knife 클래스는 Weapon 클래스를 상속받는다.
# - Knife 클래스는 객체변수로 weapon_name, power, durability를 가진다.
# - Knife 클래스의 attack 메소드는 부모 클래스의 attack 메소드를 오버라이딩하며, 
# attack이 호출될 때마다 durability가 1씩 감소한다. 그리고 `내구성 : ___`을 
# 다음 줄에 출력하며, durability가 0인 경우에는 `공격 불가!`를 출력한다.

from weapon import Weapon


class Knife(Weapon):
    def __init__(self, weapon_name, power, durability):
        super().__init__(weapon_name, power)
        self.durability = durability

    def attack(self):
        if (self.durability==0):
            print('공격 불가!')
            return
        else:
            self.durability-=1
            super().attack()
            print('내구성 %d'%self.durability)