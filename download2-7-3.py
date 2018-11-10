import bs4
import urllib.request
import urllib.parse
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

baseUrl = "https://www.inflearn.com/"
quote=urllib.parse.quote_plus("추천-강좌")
originUrl= baseUrl+quote



Url=urllib.request.urlopen(originUrl).read().decode(urllib.request.urlopen(originUrl).headers.get_content_charset()) #utf-8 byte 상태 decoding 부분

soup=bs4.BeautifulSoup(Url,"html.parser")

recommand=soup.select("ul.slides")[0] #slides class 뭉치중 첫번째만 긁어옴

for e in recommand:
    print(e.select_one("h4.block_title > a").string)
