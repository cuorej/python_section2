import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#클래스 변수, 인스턴스 변수 개중요!!!


class Warehouse:
    stock_num = 0  #class변수야 이게 바로!!!!!!!!!!!!!!
    def __init__(self, name):
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse("kim")
user2 = Warehouse("park")

print(user1.name)
print(user1.__dict__)
print(user2.name)
print(user2.__dict__)
##위에서 보면 stock_num이 보이지 않음
print(Warehouse.__dict__) # user1, user2 두번을 만들었기 때문에 stock_num=2
print(user1.stock_num) #user1은 인스턴수 변수기때문에 독립적, 하지만 .stock_num이 이 변수안에없기때문에 class 에 접근, 이 class 변수는 독립적이지 않음 공유됨
print(user2.stock_num) # 따라서 user1 user2 두개의 stock_num 은 둘다 2가 되는거임

#다시정리 (!!접근순서!!)
#인스턴스 네임스페이스 -> 클래스 네임스페이스, 클래스 변수 (공유)
