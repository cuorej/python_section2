import urllib.request
import urllib.parse

data = urllib.parse.urlencode({'id': 'yoursID', 'password': '1234'})
print('전', data)
data = data.encode('ascii')
print('후', data)
response = urllib.request.urlopen('http://www.naver.com', data)
print('response', response)
