import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl="http://cafefiles.naver.net/data27/2007/6/24/291/like79420_30.jpg"
htmlURL="http://google.com"
savePath1="c:/test1.jpg"
savePath2="c:/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') #w: write, r: read, a:add, wb:write as binary
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2: #with 벗어날때 자동으로 close가 실행됨
    saveFile2.write(f2)

print("다운완료")

'''
urlretrieve:
다이렉트로 저장-> open('r')->변수에 할당 -> 파싱 -> 저장
용도: 사자사진 단체로 1000장 다운(파싱이 필요없음)
urlopen:
저장 하기 전에 변수할당 -> 필요한 부분 파싱 -> open 통해서 db에 저장
용도: 파싱!
'''
