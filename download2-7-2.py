import bs4
import urllib.request
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

originUrl = "https://finance.naver.com/sise/"

Url=urllib.request.urlopen(originUrl).read().decode(urllib.request.urlopen(originUrl).headers.get_content_charset()) #utf-8 byte 상태 decoding 부분

soup=bs4.BeautifulSoup(Url,"html.parser")

#print("Soup", Soup.prettify())

top3 = soup.select("#siselist_tab_0 > tr")

for  e in top3:
    if e.find("a") is not None:
        print(e.select_one('.tltle').string)
