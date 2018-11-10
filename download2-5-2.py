import bs4


html='''
<html>
    <body>
    <h1>
        파이썬 BeautifulSoup 공부
    </h1>
    <p>
        태그선택자
    </p>
    <p>
        태그선택자
    </p>
    </body>
    </html>
    '''

soup=bs4.BeautifulSoup(html,'html.parser')

#print('typesoup:', type(soup))
#print('sopu:',soup)
#print('pretty:',soup.prettify()) #들여쓰기 다 자동으로해주는거(위에선 내가함)

h1=soup.html.h1
#print("h1:",h1) #h1 태그 아래로만 가져온다

print(h1.string)
print(h1)

p1=soup.html.body.p
print('p1:',p1)
p2=p1.next_sibling
print('p2:',p2) # 이건 왜그러냐면 위에보면 엔터로인해 \n을 긁어온셈

p3=p1.next_sibling.next_sibling
print('p3:',p3) #이걸해야 태그선택자를 가져옴

p4=p1.previous_sibling.previous_sibling
print('p4:',p4)  #이전이전걸 파싱해오니 파이썬beautifulsoup 공부 가져옴
