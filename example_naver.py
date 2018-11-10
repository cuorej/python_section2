import urllib.request


imgUrl="https://ssl.pstatic.net/tveta/libs/1191/1191683/67695b8ac77faba784c4_20180928143548242.jpg"
savePath1='c:/naver.jpg'

fhand=urllib.request.urlopen(imgUrl).read()

with open(savePath1,'wb') as saveFile1:
    saveFile1.write(fhand)
print("다운완료")










import urllib.request

movieUrl="https://tvetamovie.pstatic.net/libs/1209/1209123/53f4a3f17534befb3347_20180910094357270.mp4-pBASE-v0-f63850-20180910094457793_5.mp4"
savePath2='c:/naver.mp4'

fhand2=urllib.request.urlopen(movieUrl).read()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(fhand2)

print("다운완료")
