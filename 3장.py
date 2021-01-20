money=2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 머니가 2000이므로 3000보다 작으니까 저기가 false가 되어서 else구문 실행

# in 문장으로 참,거짓 정하기
pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시 가라")
else:
    print("걸어라")

# 포켓 리스트 안에 머니가 있으므로 저 문장이 참이 되어 이프 구문 실행

#pass구문 사용하기
pocket=['paper','cellphone','money']
if 'money' in pocket:
    pass
else:
    print("걸어라")
# 이러면 pass가 실행되어 아무것도 실행 안됨
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")
#if나 else구문에서 문장이 하나면 이렇게 간단하게도 실행가능!



## elif구문 그냥 else + if 된거임 전 구문이 거짓일 때 실행!
pocket=['paper','cellphone']
card=True
if 'money' in pocket:
    print("택시 가라")
else:
    if card:
        print("택시 가라")
    else:
        print("걸어가라")

pocket=['paper','cellphone']
card=True
if 'money' in pocket:
    print("택시 가라")
elif card:
        print("택시 가라")
    else:
        print("걸어가라")









for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print(' ')

#조건부 표현식
#조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우

score=60
message = "success" if score >= 60 else "failure"
message

#while문 정복

#나무 10번찍어서 넘기기
treehit=0
while treehit <10 :
    treehit=treehit+1
    print("나무를 %d번 찍었습니다." %treehit)
    if treehit==10:
        print("나무가 넘어갔습니다.")

#프린트와 저기 찍은 횟수 추가 자리를 바꾸면 0부터9가 출력 ..생각해보자


#신기하네.. number를 이제 계속 인수로 받고 4가 나오면 prompt출력을 그만 하게되는것

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number=0
while number !=4:
    print(prompt)
    number = int(input())

#커피 계산
#money를 숫자로 꼭 지정을 해야하는거 같은데 ??
money=200
coffee = 10
while coffee!=0:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break

# ?? while true는 계속 실행하기 위해서 쓴건가

# continue를 통해 while문 맨 처음으로 돌아가기
# 홀수 뽑기!
a=0
while a<10:
    a=a+1
    if a%2==0: continue
    print(a)

#for문 뿌수기
test=["one","two","three"]
for i in test :
    print(i)

marks = [90, 25, 67, 45, 80]

number=0
for score in marks :
    number=number+1
    if score >=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다."%number)


# 저기 for다음 쓰는 변수는 아무 문자여도 상관이없는거 같은데 이미 값이 저장되어있는 문자여도 for문 안에서는 무의미 ??

#위에서 변형하여 continue이용하여 합격한 사람만 뽑기
number=0
for score in marks:
    number=number+1
    if score <60:
        continue
    print("축하드립니다. %d번째 학생은 합격입니다." %number)


# range와 index이용
# range(1,11) >> 1에서부터 11까지

for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("축하합니다. %d번째 친구는 합격입니다." %(number+1))

#구구단

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print("")

#연습문제
#while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.

number=0
add=0
while number<=1000:
    number=number+1
    if number%3==0 : add=add+number
    else: continue
print(add)


#4
for i in range(1,101):
    print(i)


score=[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# 여기서 왜 한번에 실행하면 안되냐 .. ??
add=0
for i in range(len(score)):
    add=add+score[i]

add/len(score)

#
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result=[num*2 for num in numbers if num%2==1]
result


star=1
while star<=5:
    ss="*"
    s=ss*star
    print(s)
    star=star+1