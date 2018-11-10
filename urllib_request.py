import urllib.request
with urllib.request.urlopen('https://naver.com') as f:
    print("\nread:\n\n",f.read(100).decode("utf-8"))
        #100byte 읽어서 decode해 출력
    print("\ngeturl:\n\n",f.geturl())
        #검색한 리소스의 url 주소 반환
    print("\nstatus:\n\n",f.status)
        #상태반환 200:정상 404:없음 403:reject 500:compile error
    print("\nheaders:\n\n",f.getheaders())
        #헤더 정보를 리스트 형태로 반환
    print("\ninfo:\n\n", f.info())
        #html의 헤더를 포함한 meta 정보 반환
    print("\ngetcode:\n\n", f.getcode())
        #status랑 같은 역할
