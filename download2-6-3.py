import bs4


fp=open("cars.html",encoding="utf-8")
soup=bs4.BeautifulSoup(fp, "html.parser")

def car_func(selector):
    print("car_func", soup.select_one(selector).string)

#아래는 전부 같은거
car_func("#gr")
car_func("li#gr") #li tag에 id가 gr
car_func("ul > li#gr")
car_func("#cars #gr") #cars의 자손들을 찾아
car_func("#cars > #gr") #cars의 자식
car_func("li[id='gr']")
print("car_func",soup.select("li")[3].string)
print("car_func", soup.find_all('li')[3].string)



car_lambda = lambda q : print('car_lambda', soup.select_one(q).string)
#q를 selector 매개변수로 받아서 쓰는것



car_lambda("#gr")
car_lambda("li#gr") #li tag에 id가 gr
car_lambda("ul > li#gr")
car_lambda("#cars #gr") #cars의 자손들을 찾아
car_lambda("#cars > #gr") #cars의 자식
car_lambda("li[id='gr']")
