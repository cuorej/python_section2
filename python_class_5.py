import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')




class NameTest:
    total = 0


print(dir())

print("before: ", NameTest.__dict__)
NameTest.total=1
print("after: ", NameTest.__dict__)


n1= NameTest()
n2= NameTest()

print(id(n1), "vs", id(n2)) #2611702984656 vs 2611703029832 즉 주소가달름
print(n1.__dict__)
print(n2.__dict__)

print(n1.total)
print(n2.total)

n1.total=77
print(n1.__dict__)

print("last: ", n1.total) #n1 에는 클래스 영역 전에 자기 인스턴스 영역안에 total이 있기 때문에 77불러옴
print("last: ", n2.total) #n2 에는 total이 없기때문에 class 영역에서 접근함
