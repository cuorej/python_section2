import bs4


fp=open("food-list.html",encoding="utf-8")
soup=bs4.BeautifulSoup(fp, "html.parser")

print("1. ", soup.select_one("li:nth-of-type(8)").string) #조건에 맞는 한개(li 함수의 8번째)를 반환하고 스트링에 바로 접근

print("2. ", soup.select_one("#ac-list > li:nth-of-type(4)").string) #id 가 ac-list 인 것들의 자식중 li 함수의 4번째-id는 샾으로 접근

print("3. ", soup.select("#ac-list > li[data-lo='cn']")[0].string) #select는 찾아서 리스트로 반환 그들중에 data-lo 가 cn인걸찾아
 #select() 자체가 리스트형태이기때문에 select()[0] 이면 그 리스트의 첫번째걸 가져와.

print("4. ", soup.select("#ac-list > li.alcohol.high")[0].string)#alcohol high에 접근하기 위해선 스페이스바를 . 으로 대체하여 접속


param = {"data-lo": "cn", "class": "alcohol"}
print('5. ', soup.find("li",param).string) #dictionary를 파라미터로 넣어 파싱가능

print('6. ', soup.find(id="ac-list").find("li",param).string) #id 가 ac list 인 것의 자식에서 param 찾아서 파싱


for ac in soup.find_all("li"):
    print('li', ac)
    if ac["data-lo"] == "us":
        print("data-lo==us", ac.string)
