import bs4

html = """
<html><body>
<div id="main">
  <h1>강의목록</h1>
  <ul class="lecs">
    <li>Java 초고수 되기</li>
    <li>파이썬 기초 프로그래밍</li>
    <li>파이썬 머신러닝 프로그래밍</li>
    <li>안드로이드 블루투스 프로그래밍</li>
  </ul>
</div>
</body></html>
"""

soup=bs4.BeautifulSoup(html,'html.parser')

h1=soup.select_one("div#main > h1") #div 안에 main이란 id를 가진 하위에 h1

print('h1:',h1.string)

list_li = soup.select("div#main > ul.lecs > li")

for li in list_li:
    print (li.string)
