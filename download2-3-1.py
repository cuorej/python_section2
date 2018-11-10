<<<<<<< current
import sys
import io
import urllib.request as req
import urllib.parse
#from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url="http://www.encar.com"

mem = req.urlopen(url)

#print(type(mem))


#print("geturl",mem.geturl()) #검색한 리소스의 URL 반환
#print("status",mem.status) #200:정상, 404:없음, 403:reject, 500:compile error
#print("headers",mem.getheaders())
#print("info",mem.info()) #header, meta 정보를 반환
print("code", mem.getcode())
#print("read", mem.read(50).decode("utf-8")) #50byte만 읽고, utf-8로 디코딩
                                    #utf-8 디코딩시 너무 크면 안됨 traceback 걸림
print(urllib.parse.urlparse("http://www.encar.com")) #import 값 새로 해줘야함
=======
import sys
import io
import urllib.request as req
import urllib.parse
#from urllib.parse import urlparse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


url="http://www.encar.com"


mem = req.urlopen(url)

#print(type(mem))


#print("geturl",mem.geturl()) #검색한 리소스의 URL 반환
#print("status",mem.status) #200:정상, 404:없음, 403:reject, 500:compile error
#print("headers",mem.getheaders())
#print("info",mem.info()) #header, meta 정보를 반환
print("code", mem.getcode())
#print("read", mem.read(50).decode("utf-8")) #50byte만 읽고, utf-8로 디코딩
                                    #utf-8 디코딩시 너무 크면 안됨 traceback 걸림
print(urllib.parse.urlparse("http://www.encar.com")) #import 값 새로 해줘야함
>>>>>>> before discard
