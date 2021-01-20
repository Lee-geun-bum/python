#클래스

result=0
def add(num):
    global result
    result += num
    return result

add(1) #1
add(2) #3
add(3) #6
# global을 활용하여 밖에있는 result를 바꿔주었다 그리고 점점 늘어나는 형식
# 라잌 계산기

#클래스는 이런느낌!!
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

# cal1,2는 calculator 클래스의 인스턴스가 된다!
# cal1,2는 객체 ,, 클래스로 객체들을 생성 . 생성된 객체들은 그 클래스의 인스턴스

#사직연산 클래스 활용!!!
class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def min(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

a=FourCal() #이렇게 함으로써 a.함수를 호출 가능 저 클래스 안의

a.setdata(2,4)
a=FourCal(2,4) #이렇게 init을 사용하여 바로 할수도있음 이게 난거같아
#요거 두개는 똑같은거

#a.first=2
#a.second=4
b=FourCal()
b.setdata(3,7)
b.first  # a.first와 b.first는 독립이다 !!

a.div()

#클래스 상속하기 좋네 이런건
class MoreFourCal(FourCal):
    pass

#이러면 일단 두 클래스는 같은 역할이고 저기에 추가해서 fourcal보다 
#많은 함수를 실행하는 클래스를 만들어냄.. 오 패키지 같네

#기능 추가 !
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result

a=MoreFourCal(3,4)
a.pow()
# 제곱기능 추가 !! a**b 는 a의 b제곱

## 매서드 오버라이딩 ! 이제 상속해서 매서드를 수정하는 거지

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

#수정하였으면 수정한 클래스로 꼭 실행해야함
# 오버라이딩 할땐 매서드 명을 같게!
a = SafeFourCal(4, 0)
a.div()
a = FourCal(4, 0)
a.div()  # 이건 0으로 못나누니까 오류!!


C:\doit>python

import mod1.py

import os
os.chdir('C:\doit')
# 대화형 인터프리터에서 경로바꾸기 !

sys.path.append
# 경로 추가해주기! 이러면 바로 모듈 실행 가능

# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려줌 !

#모듈 패키지 하나도 모르겠노 ㅅㅂ..

#예외 처리!

f=open("none",'r')
#디렉토리 안에 없는 파일을 열려고했을때 이렇게 뜸
#이 외에도 뭐 없는 인덱스 실행 ,, 0으로 나누기

#오류 예외처리하기
#try,except문

try:
    4 / 0 #오류가발생하는 문장
except ZeroDivisionError  as e:
    print(e)

#except 발생 오류 as 오류 메시지 변수:

#finally절 사용

f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
#이런식으로 try의 문장수행후에 마지막에 닫아줌 f를 !

#여러개의 오류 처리
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

# 인덱싱 할 수 없습니다. 만 출력됨.!
# 이 경우는 인덱싱오류가 먼저 나기때문에 제로디비션에러는 실행안됨
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)
#이렇게 (,)묶어주면 한번에 처리가능!
#근데 왜 하나만 출력되지 ??

except FileNotFoundError:
    pass
# pass를 해줌으로써 저 에러가 났을때 그냥 통과시키는거!

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

class Bird:
    def fly(self):
        raise NotImplementedError
        #이부분은 raise를 통해 오류가 뜨게 만들어주는거
        #의미는 bird클래스를 상속받는 자식 클래스 안에 fly가 없다면 저 에러가 뜨게 만들어준다잉
        #여기서 에러가 안나려면 저기 eagle클래스 안에 fly매서드가 있어야지


