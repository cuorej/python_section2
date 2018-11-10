from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#아래 세줄은 헤더정보를 심어서 user-agent 정보를 같이 보내는 코드
opener = urllib.request.build_opener()
opener.addheaders = [("User-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36")]
urllib.request.install_opener(opener)

base= 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%82%AC%EC%9E%90'
quote=urllib.parse.quote_plus('사자')
url=base+quote
#print(base)

res=urllib.request.urlopen(url)
savePath="C:\\imagedown\\" # c:\imagedown\ 윈도우에선 이거도 괜츈

try:
    if not (os.path.isdir(savePath)): #savePath 루트가 없다면
        os.makedirs(os.path.join(savePath)) #폴더를 만들어

except OSError as e:
    if e.errno != errno.EEXIST:  #강의 자료에 error에대한 링크 읽으면 이해가능
        print("폴더만들기 실패!")
        raise


soup = BeautifulSoup(res, "html.parser")

img_list = soup.select("div.img_area > a.thumb._thumb > img")

for i, img_list in enumerate(img_list,1):
    #print(img_list['data-source'])
    fullFileName = os.path.join(savePath, savePath+str(i)+'.jpg') #파일이름 주르륵 정하고 나오게)
    urllib.request.urlretrieve(img_list['data-source'],fullFileName) #urlretrieve 는 (다운받을주소,다운받은파일의 이름)

print("다운로드 완료")
