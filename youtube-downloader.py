import pytube
import os
import subprocess  #터미널안에서 명령어를 실행할수 있고 그 반환값을 가져올수 있음

youtubeUrl = pytube.YouTube("https://www.youtube.com/watch?v=fB8TyLTD7EE")#다운받 동영상 URL 지정
videos=youtubeUrl.streams.all()



for line in range(len(videos)): # range(1,6) >>1,2,3,4,5,6 #range(3) >>0,1,2,3

    print (line,videos[line])

cNum =int(input('머받을래? :'))

if cNum==94:
    quit()


down_dir="c:\youtube"


videos[cNum].download(down_dir)

newFileName=input("변환받을 mp3파일명?:")
oriFileName=videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
]) #"c:\youtube\maroon5.mp4"
