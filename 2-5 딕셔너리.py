# 딕셔너리의 기본 툴
#{Key1:Value1, Key2:Value2, Key3:Value3, ...}

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}


#딕셔너리 쌍 추가하기 그냥 인덱스해서 넣으면됨 
#>>> a = {1: 'a'}
#>>> a[2] = 'b'
#>>> a
#{1: 'a', 2: 'b'}
# a[key]=value
# value는 리스트도 가능@!

#쌍 삭제
# del a[key]하믄 됨

#value추출
#a[key]하면 된다눈뎅


a = {1: 'a',1:'b',1:"c"}
#같은 키는 다 제외하고 마지막꺼만 출력... 그니까 저거실행하면 1:'c'만


#key 추출
#a.keys(),,,,,, list앞에 씌어주면 리스트로 출력 key를 
#a.value()도 가능.

#쌍 추출
#a.items() 쌍으로 추출해준다잉

#다 지우기는 a.clear()

# a.get('foo', default) 이건 a의 foo의 벨류 추출하는거 없으면 저 default출력

# 'name' in a <<a의 key중 name이 있는지 조사 있으면 트루!

#집합 자료형 ?

s1=set([11,1,2,3])
s1=set([12,1,2,3,11,5])
s1=set([3,2,1])
s1
# 이건 {1,2,3} 이 되는 거임
# 음 무슨 기준으로 출력되는건진오르겠네 순서가없네 .. 

#>>> s2 = set("Hello")
#>>> s2
# {'e', 'H', 'l', 'o'}   아 이런식으로 원소 추출.. ㅇㅋ

#중복을 제외하고 싶을 때 종종 쓰이는 거구만... 인덱스 지원 ㄴㄴ

s1 = set([1, 2, 3, 4, 5, 6])

s2 = set([4, 5, 6, 7, 8, 9])

# s1 &s2 교집합 구하는게 가능하네 합집합은 | 이고
# s1.intersection(s2) ,,,,, s1.union(s2)
# s1-s2 로 차집합도 가능
# s1.difference(s2)


#집합 자료형에 값 추가하기

#s1.add(4) 하면 s1에 4가 추가되는거임
#s1.update([4, 5, 6]) 이거는 여러개 추가하기

s1.remove(2)
s1.remove(3)

s1.discard(2)


#불 자료형 : 트루랑 폴스로만 나타남


#q8뭐징

#q9
#1번,4번은 저 키가없고, 키의 형태가 리스트면 안된다(변할수있으니까)
#3번은 없어서그런건가..



#q12는 아이디가 같아서..? id()가 같아서 같은 자료를 부르는 변수가 2개인거지
#그래서 자료가 바뀌면 둘다 바뀌는거아닌가 




a=dict()
a['name'] = 'python'
a


score=[80,75,55]







