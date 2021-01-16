hello.hi
print("Hello World")

a=4.24e10
4.24*10^10

b=0o177
8진수 표현 0+o

x**y == x^y

 % == 나머지반환
 / == 나누기
 // == 몫 반환



 문자열

say1 = 'Python\'s favorit food is perl'
say = "Python's favorite food is perl"
say2 = 'Python\'s favorit food is perl'
 백슬래쉬로 저렇게 넣을 수도 있음

life = "Life is too short\nYou need python"
life1 = '''    Life is too short    You need python    '''
life2='''
... Life is too short
... You need python
... '''


head="python"
tail=" is fun!!"
head+tail
ㅋㅋ더하기도 되고 곱하기도됨




a="Life is too short, You need Python"

a[3]은 저 4번째 인 e가 출력 파이썬은 0부터셈 숫자를 입감?
a[-1]은 뒤에서 부터 1번째가 되는거임..
-0과0은 같으므로 a[0]은 첫번째 문자ㅇ이고 a[-1]이 뒤에서 첫번째 문자
오 a[0:4]이면 4는 포함안함... 즉 a[0~3]이 출력된다잉 이점 유의



a = "Pithon"
a[:1]
'P'
a[2:]
'thon'
a[:1] + 'y' + a[2:]
'Python'

문자열을 바꾸고싶다면 이렇게 해야한다잉
 r 처럼 원래 지정되어있는 문자를 못바꾼데 a[1]<-"y"가 안됨!


문자열 포맷 코드 !

"I eat %d apples." % 3
'I eat 3 apples.'

"I eat %s apples." % "five"
'I eat five apples.'

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'

 %d =정수, %s = 문자열
%s는 숫자여도 그냥 문자취급해서 넣어버림 그래서 유용한듯..
포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다.

포맷함수활용
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
'I ate 10 apples. so I was sick for three days.'


정렬하기 길이를 10으로 !
"{0:=^10}".format("hi")
'====hi===='
"{0:!<10}".format("hi")
'hi!!!!!!!!'

f문자열 활용
age = 30
f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'



a.count('b')
#a에서 문자b의 개수 반환
a.find('b')
#a에서 문자b가 처음 나온 위치 반환, 없으면 -1반환
a.index('t')
#a에서 문자t가 처음 나온 위치 반환, 없으면 에러

#조인함수
",".join(['a', 'b', 'c', 'd'])
#'a,b,c,d'








