import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl="http://cafefiles.naver.net/data27/2007/6/24/291/like79420_30.jpg"
htmlURL="http://google.com"
savePath1="c:/test1.jpg"
savePath2="c:/index.html"


dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL,savePath2)
print("다운완료")

print("hi")
