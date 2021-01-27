abs() #절댓값돌려줌
all()#반복가능한 자료형 요소가 모두 참이면 true 거짓이 하나라도 잇으면 false
     # 0은 false값
any()# all의 반대!..? 모두 거짓이면 false
chr()#아스키 코드... 0~127를 문자나 기호에 대응시켜놓음
ord()# 아스키 코드값을 돌려줌 위에꺼 반대
dir()#dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
     #이거는 좋은듯
divmod(10,3)  # =(3,1) >>>>> (몫,나머지) 반환

enumerate(['body', 'foo', 'bar'])
for i,name in enumerate(['body', 'foo', 'bar']):
    print(i,name)
# 이롷게 실행하네 열거하다라는 뜻임 enumerate

eval('1+2') # >>3출력 ,, 실행가능한 문자열을 받아 직접 실행한 결과값을 돌려줌!
print('1+2')# >>1+2 출력

filter()
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
# 필터의 의미는 2번째 인수를 1번째 인수의 함수에 넣었을때 참값만 걸러줌!!
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
#이렇게 def안쓰고 간단하게 하고싶을때 요롷게 lambda를 활용가능

a=input()
b=input("ENTER:")

#id가 다르넹..

int('3') #문자열 형태나 소수점이 있는 숫자를 정수형태로 돌려줌!!
int('11', 2) #3,, 2진수로 표현된 11을 정수로 바꿔줄수도있음

str() # 인수를 문자열 형태로 변환하여 돌려줌!!

#isinstance(object,class)  첫번재 인수가 2번째 클래스의 인스턴스인지 판단 !

#map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
# map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수이다.

list(map(lambda a: a*2, [1, 2, 3, 4]))
# ===[2, 4, 6, 8]

range(1,10,2) # range활용 마지막인수는 간격!! 공차 느낌이지






















































































#연습문제
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCaluator(Calculator):
    def minus(self,val):
        self.value -=val

# 뭔소린지 잘 이해가 안가노 ..
cal=UpgradeCaluator()
cal.add(10)
cal.minus(7)
cal.value


#2
class MaxLimitCalculator (Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            return 100
        else:
            self.value += val

cal=MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)




# 4

list(filter(lambda x:x>0,[1, -2, 3, -5, 8, -3]))

#5
int('0xea',16)

#6
list(map(lambda x:x*3,[1,2,3,4]))
#8
round(17/3,4)
#9


#11
#glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성해 보자.

import glob
glob.glob('C:\doit\*.py')


import time
year=time.strftime('%Y', time.localtime(time.time()))
year=time.strftime('%Y', time.localtime(time.time()))
#2018/04/03 17:20:32

