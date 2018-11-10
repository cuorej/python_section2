import bs4
import re

html = """
<html><body>
  <ul>
    <li><a id="naver" class="sister" href="http://www.naver.com">naver</a></li>
    <li><a class="sister" href="http://www.daum.net">daum</a></li>
    <li><a class="sister" href="https://www.google.com">google</a></li>
    <li><a class="sister" href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup=bs4.BeautifulSoup(html,'html.parser')

print(soup.find(id="naver").string) # id로 string 파싱

li=soup.find_all(href=re.compile(r"^https://"))
print("li:",li) #list 값으로 반환

for e in li:
    print(e.attrs['href'])
