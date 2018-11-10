import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class SelfTest:
    def function1():
        print("function1 called!")

    def function2(self):
        print("function2 called!")


f = SelfTest() #SelfTest를 매개변수로 넘겨서 인스턴스 생성
print(dir(f)) #파이썬이 제공하는 필드들과 우리가 만든 function1 과 function2 가 정의되어잇을거임

#f.function1() #>>TypeError: function1() takes 0 positional arguments but 1 was given 라고뜸
              #TypeError: function1() takes 0 positional arguments but 1 was given 이게뭔말이냐면.. 우리가만든건 0개의 argument를 받기로되어잇는데 1개가 넘어온거임.

print(SelfTest.function1()) # f 변수없이 바로 불러들이면 됨 None 뜸!! class의 이름으로 접근함 이경우는



#print(id(f)) #2609908215592 주소값
#f.function2()
