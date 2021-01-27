# 6장 파이썬 프로그래밍

#2단 만들기 ! 구구단
from typing import List, Any
ad=range(1,10)

n=1
def GuGu(n):
    for i in range(1,10):
        gu=n*i
        gu=list(gu)
    return gu

result = GuGu(2)

# 지금 이건 왜 에러지 ??
# gu가 어떤건지 미리 정해줘야하는듯
def GuGu(n):
    gu=[]
    for i in range(1,10):
        gu.append(n*i)
    return gu
#이렇게하면 에러안뜸 저 append는 뭐 추가 이런의미

def GuGu(n):
    print(n)

def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

result = GuGu(2)


#1000미만에서 3과 5의 배수 합하기 ..

i=1
number=0
while i<1000:
    add=0
    if i%3==0:
        number=i
    add+=number
    print(add)

#이건 뭐한건지모르겠는데..

add=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        add+=i
print(add)