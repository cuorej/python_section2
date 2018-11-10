import bs4
import urllib.request
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

originUrl = "https://www.daum.net/"




Url=urllib.request.urlopen(originUrl).read().decode(urllib.request.urlopen(originUrl).headers.get_content_charset()) #utf-8 byte 상태 decoding 부분

soup=bs4.BeautifulSoup(Url,"html.parser")

hot_issue=soup.select_one("ol.list_hotissue.issue_row").select("a.link_issue")




for number, issue in enumerate(hot_issue, 1):
    print(number, issue.attrs['href'], " + ", issue.string)
