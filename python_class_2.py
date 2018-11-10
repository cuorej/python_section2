import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


class UserInfo:
    #def set_info(self, name, phone): <<<원래 이건데 init을 쓰면..
    def __init__(self, name, phone):  ### init에 의해 class 부르자마자 초기화되니
        self.name = name
        self.phone = phone

    def print_info(self):
        print("-----------")
        print("Name: "+ self.name)
        print("Phone: "+ self.phone)
        print("-----------")


user1=UserInfo("kim", "010-3433-7777")    #__init__으로인해 이런식으로 여기서 지정
user2=UserInfo("park", "010-7777-7777")

print(id(user1)) #user이 생성된 저장소
print(id(user2))

#user1.set_info("kim", "010-3433-7777")
#user2.set_info("park", "010-7777-7777")

user1.print_info()
user2.print_info()

print(user1.__dict__)  #{'phone': '010-3433-7777', 'name': 'kim'} dict 만들어줌
#따라서 이렇게 접근해도 접근가능
print(user1.phone, user1.name)
