# - Gun 클래스는 Weapon 클래스를 상속받는다.
# - Gun 클래스는 객체변수로 weapon_name, power, bullet_num을 가진다.
# - Gun 클래스의 attack 메소드는 부모 클래스의 attack 메소드를 오버라이딩하며,
# attack이 호출될 때마다 bullet_num이 1씩 감소한다. 그리고 `남은 총알 : ___` 을 
# 다음 줄에 출력하며, bullet_num이 0인 경우에는 `공격 불가!`를 출력한다.
# - Gun 클래스의 reload 메소드는 추가할 총알의 양을 매개변수로 받아 그 만큼 
# bullet_num에 추가한다.

from weapon import Weapon


class Gun(Weapon):
    def __init__(self, weapon_name, power, bullet_num ):
        super().__init__(weapon_name, power)
        self.bullet_num = bullet_num

        
    def attack(self):
        if (self.bullet_num==0):
            print('공격 불가!')
            return
        else:
            self.bullet_num-=1
            super().attack()
            print('남은 총알 %d'%self.bullet_num)

    def reload(self, num):
        self.bullet_num += num