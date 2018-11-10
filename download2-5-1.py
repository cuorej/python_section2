import urllib.parse

baseUrl="http://test.com/html/a.html"

print(">>",urllib.parse.urljoin(baseUrl,"b.html"))
print(">>",urllib.parse.urljoin(baseUrl,"sub/b.html"))
print(">>",urllib.parse.urljoin(baseUrl,"../index.html"))

'''
>> http://test.com/html/b.html
>> http://test.com/html/sub/b.html
>> http://test.com/index.html
'''
