import bs4

html = """
<html><body>
  <ul>
    <li><a class="sister" href="http://www.naver.com">naver</a></li>
    <li><a class="sister" href="http://www.daum.net">daum</a></li>
    <li><a class="sister" href="https://www.google.com">google</a></li>
    <li><a class="sister" href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = bs4.BeautifulSoup(html,'html.parser')

print('soup',soup)


links=soup.find_all('li > a') #a tag를 한버에 가져와: 선택자 a
links2=soup.select('li > a')

print ("find", links)
print ("select", links2)

'''
for a in links:
    href=a.attrs['href'] #a 선택자 안 속성중 href 속성 파싱
    print('htref',href)
    txt=a.string # a 선택자 안에 string
    print('txt',txt)
'''


''' 이렇게 하는방법도 존재

a=soup.find_all("a", string="daum") #string 이 daum인 a 선택자 내용을가져와
'''
