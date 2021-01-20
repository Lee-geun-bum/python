#파이썬 함수의 구조
#def 함수명(매개변수):
#    <수행할 문장1>
#    <수행할 문장2>
#    ...

#def add(a,b):
#    return a+b

#a=124
#b=123124
#c=add(a,b)
#c

print(add(3, 4))  # 3, 4는 인수
def add(a, b):  # a, b는 매개변수
    return a+b

def add(a, b):  # a, b는 매개변수
    return print(a+b) # 요롷게하면 바로 출력

#인수가 없는 함수
def say():
    return 'hi hello'
say()


#결과값이 없는 함수 유의!
def multi(a,b):
    print("%d와 %d의 곱은 %d입니다."%(a,b,a*b))

multi(7,6)
a=multi(7,6) #둘다 똑같이 print문장이 실행됨
print(a) #하면 none이 뜨는데 이유는 저 함수의 결과값이 없기때문!
         #print문장은 함수의 수행할 문장인거지 결과가아님 함수 결과는 return으로 반환해야함 !


#매개변수 직접 지정 호출
result=add(b=5,a=3)
print(result)
#직접 지정해주면 순서에 제약을 안받는다는 장점이 있음 !

#여려개의 인수를 받는 함수
def add_m(*nums):
    result=0
    for i in nums:
        result=result+i
    return result

# 함수이름이나 저기 *nums에서 nums부분은 맘대로 지정가능!
# 매개변수 이름 앞에 *을 붙이면 입력값을 모두 보아서 튜플로 만들어줌!
# add_m(1,2)=3  요런식으루 , 여기서 nums=(1,2)가 되는거임

# 오 변수+저런 매개변수
def add_mul(choice,*nums):
    if choice=="add":
        result=0
        for i in nums:
            result=result+i
    elif choice=="mul":
        result=1
        for i in nums:
            result=result*i
    return result

add_mul("mul",1,2,3,3)
#요런식으로 실행하는거네 앞에변수 지정하면 저렇게 그냥 *nums부분은 쉼표로 해도되는거네
#쉽게 잘알려주는구만 좋네

#키워드 파라미터 kwargs

def kwargs(**kwargs):
    print(kwargs)

kwargs(a=2)
kwargs(name="kn",age=19)
# 키워드 파라미터 사용하기 위해서는 저렇게 매개변수앞에 **붙이면됨
# 여기서도 kwargs는 맘대로 지정해도 무관 !
# 키워드 파라미터는 저런식으로 인수를 받고, 딕셔너리형태로 저장됨!

## return 관련
# 함수의 결과값은 항상 언제나 하나!

def addmul(a,b):
    return a+b,a*b
addmul(3,5)
# (8,15)형태로 튜플로 묶어서 하나로 출력됨!!
result1,result2=addmul(3,5)
result1,result2
# 뭐 이렇게하면 각각의 결과를 저장할 수 있음

def addmul2(a,b):
    return a+b
    return a*b
# 이 함수의 경우는 a+b값만 결과로 ,, 당연 return뜨는 순간 함수가 끝남 뒤에 리턴은
# 의미 없는거임

#return으로 일부로 함수 빠져나가기 즉, 특정변수값에서의 함수값 출력 x
def nick(nick):
    if nick=="멍청멍청":
        return
    print("당신의 별명은 %s 입니다." %nick)

nick("바보") # 당신의 별명은 바보입니다. 가 출력
nick("멍청멍청") # 이거는 출력이 안됨 !! 아무것도 안나옴 이케 ..

# 이 함수에서 주의할 점은 역시 결과값이 없는 함수임
# 수행할 문장에서 print가 있어서 출력값은 나오지만 결과값 자체는 없는함수!!!


#매개변수 초깃값 미리설정
#2학기 통패 함수 배운거랑 그래도 많이 비슷하네 다행이군
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("춘봉박",19)
# 마지막 매개변수를 지정안해주면 함수정의할때 지정한 초깃값 true를 따름


# 함수 안에서 선언한 변수의 효력범위 쫌 신기하네 중요한듯
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)

# 뭐가나올까
# a=1이 나온다.
# 사실 저기 함수에서 인자로 받는 a와 밖에서 지정한 a는 같은게아님 다른거임!!
# 함수만의 변수이기 때문에 함수밖에서의 a의 값은 변하지 않음..
# 함수값을 원래의 여기 작업공간에 저장하고 싶다면 따로 지정해야한다는 뜻인거같음
# >>>> 아 이건 return을 통해 지정가능 즉 바꿀수있음 원래의 변수를 함수값으로나온
#변수로

a = 1
def vartest(a):
    a = a +1
    return a
#이제 a=2가 된다!!
# return a의 뜻이 >>> a = vartest(a) 이게 된다고 이해하면 될듯. .

a = 1
def vartest():
    global a
    a = a+1
# 글로벌이라는 뜻이 밖에서의 a를 가지고 실행한다는 뜻인거 같음.. ??
# 이것도 마찬가지로 a=2가 된다잉
vartest()
print(a)

# def쓰기가 어려운경우
add = lambda a, b: a+b
result = add(3, 4)
print(result)
# add가 인수를 두개를받고 두개를 합하는 함수가 되는 거임 !
#lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식


#사용자가 입력한 값을 변수에 대입하기 !!
#콘솔창에서 입력한것이 변수로 대입되는 그런 느낌인거같음
a=input()
Life is ssshort
a # input()은 입력되는 모든것을 문자로 취급하여

number=input("입력한 숫자가 저장됩니다.")
3
number # number='3' 이 된다 !! 역시 문자로 저장됨

f=open("C:\doit\새파일.txt",'w')
# 마지막 변수 r:읽기모드, w:쓰기모드, a:추가모드
f.close()
# 파일을 닫아주는 코드

f=open("C:\doit\새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
# 닫아야 실시간으로 저장이 됨. 파이참 끄면 자동 닫힘

#외부 파일 읽는법! read.txt이런건가

f=open("C:\doit\새파일.txt",'r')
line=f.readline()
print(line)
f.close()

#모든줄읽기
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
# readline함수는 읽을 줄이 없으면 빈 문자열""를 반환
# print 전까지만 실행했을때는 line=''이 반환된다
# 즉, 마지막꺼가 저장된다는 이말인건가 반복하다가 ??
f.close()

f = open("C:/doit/새파일.txt", 'r')

while lines!="":
    lines = f.readlines()
    print(lines)
# 이건 왜 안될까 ??

while 1:
    data=input()
    break
    print(data)
# 이걸 왜한건지 잘모르겠는데

f.close()

f = open("C:/doit/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
# readline 은 애초에 한문장만 읽는건가.. 그래서 lines로 하면 다출력됨

f = open("C:/doit/새파일.txt", 'r')
data=f.read()
print(data)
# 뭐야 이런게 있구만 ... read는 data전체를 문자열로 반환해줌

# 파일에 새 내용 추가하기!
f = open("C:/doit/새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()
# 이렇게하면 11번째 부터 19번재 줄입니다가 추가 원래 그거에!
# 저기 오픈 마지막 인수를 'w'하면 원래의 데이터는 초기화됨.

#모듈 맛보기

import sys

args=sys.argv[1:]
for i in args:
    print(i)


f = open("C:/doit/sys1.py", 'w')
f.close()




## 연습문제

#주어진 자연수가 홀수인지 짝수인지
def is_odd():
    number=input()
    if number%2==0:
        print("%d 는 짝수입니다."%int(number))
    else :
        print("%d는 홀수입니다."%int(number))
# 이거는 왜 오류가 나지 .. ??
def is_odd1(a):
    if a%2==0:
        print("%d는 짝수입니다."%a)
    else :
        print("%d는 홀수입니다."%a)


#입력으로 들어오는 모든 수의 평균 계산

def mean(*nums):
    mean=sum(nums)/len(nums)
    return mean
#3번

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" % total)


#4번
print("you" "need" "python")
print("you"+"need"+"python")
print("".join(["you", "need", "python"]))
print("you", "need", "python") #요거는 ,로 했을때 띄어쓰기하고 합쳐줌

#5번
f1 = open("C:/doit/test.txt", 'w')
f1.write("Life is too short")
f1.close()
f2 = open("C:/doit/test.txt", 'r')
print(f2.read())

#그냥 안닫고 실행해서 그런거네 근데 17은 뭐지 왜 길이를 반환하지

#6번

f3=open("C:/doit/test.txt",'a')

addd=input("추가할 문장 입력")

f3.write(addd)
f3.close()
# r근데 write함수 쓸때 자꾸 왜 길이가 반환되는거임 ??


#6번
f3=open("C:/doit/test.txt",'a')
for word in f3:
    word.replace("java","python")
    f3.write(word)
f3.close()



a.replace("java","python")

#음 어캐했냐 ??