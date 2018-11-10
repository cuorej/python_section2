import bs4
import urllib.request
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

originUrl = "http://finance.daum.net/"

Url=urllib.request.urlopen(originUrl).read() #utf-8 byte 상태

Soup=bs4.BeautifulSoup(Url,"html.parser")

#print("Soup", Soup.prettify())


top=Soup.select("ul#topMyListNo1 > li") #select 는 list
top2=Soup.find_all("ul#topMyListNo1 > li")

for i,e in enumerate(top,1):
    print(i, e.find("a").string, e.find("span").string,e.select_one("span > span").string) #e는 한줄한줄에 대해 다시 bs4 요소이다.
