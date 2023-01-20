# import requests
# url = 'https://api.agify.io?name=seungtae'
# result=requests.get(url).json()
# print(result)
# print(result['age'])

# url='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1049'
# ////////////////////
# import requests
# hoicha=input()
# url ='https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo='+str(hoicha)   # f'  ' (hoicha)

# result=requests.get(url).json()
# print(result)
# for i in range(1,7):
#     words="drwtNo"+str(i)
#     print(result.get(words))i
# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number = number +1
#     if mark >= 60:
#         print("%d번 학생은 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# add= 0
# for i in range (1,11):
#     add=add+i
#     print(add)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end=' ')
# #     print('')
# t=int(input())
# for i in range(1,t+1):
#     a=list(map(int,input().split()))
#     a.sort(reverse=True)
#     print(a)
#     print(1,a[0])

#t라는 숫자는 
# a=3
# b=5
# 3+5=8입니다

# a=3 
# # b=5
# # print(f'{a}+{b}={a+b}입니다')
# # print("""오늘은"100%"\n입니다""")
# s="abcdefg"

# print(s[5:2:-1])
# # print(s[1:5:2])
# a,b=0,-1
# a,b=bool(a),bool(b)
# print(a,b)
# # lst=[1,2,3,4,5]
# # print(*lst)
# # print(lst)
# tp=(1,2,3,4,5)
# print(tp)
# print(type(tp))
# print(len(tp))
# print(tp[-1])
# a=int(input())
# b=int(input())

# result=(a//b+(bool(a.b)))
# # print(result)
# person1 = input("김코딩")
# person2 = input("이싸피")
# # print("""'김코딩'

# sum=0
# for i in range(2,1000,2):#2의배수
#     sum=sum+i


# for j in range(7,1000,7):#7의배수


# # sum=0
# # for i in range(2,10,2):
# #     sum = sum+i
# # print(sum)

# #값추가
# s={1,2,3,4,5}
# s.add(6)#1개 추가
# s.update([11,12,8,7,6])#여러개 추가

# #값 삭제
# s.remove(6)
# print(s)
# s.discare(12)
# print(s)
# s.clear()#다 삭제
# print(s)
    

# #값추가
# s={1,2,3,4,5}
# s.add(6)#1개 추가
# s.update([11,12,8,7,6])#여러개 추가

# #값 삭제
# s.remove(6)
# print(s)
# s.discare(12)
# print(s)
# s.clear()#다 삭제
# print(s)

# #집합
# s1=[1,2,3,4,5]
# s2=[2,4,6,8]
# #교집합
# s1,s2=set(s1),set(s2)
# print(s1&s2)
# #합집합
# print(s1|sw)
# print(s1.union(s2))
# #차집합

# set2= set(range(2,1000,2))
# set7= set(range(7,1000,7))
# lst=(set2|set7)
# print(sum(lst))
# ans_lst=[]
# for i in range(1000):
#     if i%2==0 or i %7==0:
#         ans_lst.append(i)
# print(sum(ans_lst))
# m = 5
# n = 4
# print((('*'*n)+'\n')*m)
# m=5
# n=4
# for i in range(m):
#     print('*'*n)

#알고리즘 90
#파이썬과먹좀수 80아닌 85점
#전체과목 평균
# score = {
#     'python': 80,
#     'django': 89,
#     'web': 83
# }
# score['python']=85
# score['algorithm']=90
# a=score.values()
# b=sum(a)/len(a)
# print(b)

#사용자가 입력한 각 자릿수를 더해 출력하는 코드를 작성하라

# s=input('숫자를 입력해주세요:')
# n=len(s)
# print(n)

# s=input('숫자를 입력해주세요:')
# for i in range[0:]:
#     print(i)

#     n= int(input())
# sum=0
# for i in str(n):
#     sum+=int(i)

# print(sum)

# n= int(input())
# sum=0
# for i in str(n):
#     sum+=int(i)

# print(sum)

 #리스트 반복문 만들기 %10하고 //10하고 하는 반복문 만들기
            #리스트 값 더한거 만들기

# num=int(input())
# if num % 2 == 1: #num % 2:
#     print('홀수')
# else:
#     print('짝수')
    
# dust=500
# if dust > 150:
#     print('매우나쁨')
#     if dust > 300:
#         print('실외 활동을 자제하세요.')
# elif dust > 80:
#     print('나쁨')
# elif dust > 30:
#     print('보통')
# elif dust >= 0:
#     print('좋음')
# else:
#     print('입력오류')
# print('미세먼지 확인 완료!')

# num = 2
# if num % 2:
#     result = '홀수입니다'
# else:
#     result = '짝수입니다'
# print(result)

# num = 2
# result = '홀수입니다'if num % 2 else '짝수입니다'
# print(result)
# #falsy []{}()'' 비어있는 값은 falsy
#for문 반복횟수 알고있을때 while 반복횟수 모를때
# a=0
# while a < 5: #종료조건
#     print(a)
#     a += 1  #반복시 a가 계속 증가
# print('끝')

# for fruit in ['apple','mango','banana']:
#     print(fruit)
# print('끝')

# a=int(input())
# if a>5:
#     print('오삼')
# elif a>3:
#     print('불고기')
# elif a>4 or a==-1:
#     print('재시도')
# else:
#     print('오삼불고기')

# a=int(input())
# b=int(input())
# if a>b:
#     print(a)
# else:
#     print(b)

# result=a if a>b else b#조건표현식  if 다음에 들어가는 조건이 참이면 앞에값 반환
# print(result)           #거짓이면 뒤에값 반환


# for i in range(1,101):
#     print(i,end=' ')

# for i in range(1,101):
#     print('#',end=' ')
# i=1
# while i<101:  #while 조건: whole의 조건이 참인 동안에 코드를 실행하라
#     print(i,end=' ')
#     i=i+1    #i+=1

# lst=[[1,2,3],[4,5,6]]

# print(lst[0][1])

# for i in range(0,2):
#     for j in range(0,3):
#         print(list[i][j],end=' ')
#     print()

# lst=[[1,2,3],[4,5,6]]
# multi=[]
# for i in range(2):
#     for j in range(3):
#         multi.append(lst[i][j]**2)
# print(multi)

# for i in multi:
#     print(i,end=' ')

# lst=[[1,2,3],[4,5,6]]
# multi=[]
# for i in range(2):
#     temp=[]
#     for j in range(3):
#         temp.append(lst[i][j]**2)
#     multi.append(temp)
# print(multi)


# #딕셔너리

# di={'kevin':1,'john':2,'bob':2}
# # print(di)
# for i in di:
#     # print(i,di[i])
#     # print(i,di[i])
#     print(i,di[i])
# for i,j in di.items():
#     print(i,j)
#break 반복문을 중간에 멈추고 싶을때 for while(break는 함수 종료가 아님!)
#return 함수의 값을 반환하거나 또는 그냥 함수 종료

# lst=[1,2,3,4,5,6,7]
# for i in lst:
#     if i==5:
#         break
# print(i,end=' ')
# lst=[[1,2,3,],[1,2,3,],[1,2,3,]]
# for i in range(3):
#     for j in range(4):
#         if lst[i][j]==3:
#             break
#         print(lst[i][j],end=' ')
#--------------------------------
# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# b=orders.count('아메리카노') 
# c=orders.count('마키야또') 
# d=orders.count('아이스라떼')
# e=orders.count('에스프레소')
# f=orders.count('핫초코')
# g=orders.count('카푸치노')
# print(b+c+d+e+f+g)
# result=[]
# a=orders.split(',')

# for i in a:
#     if i not in result:
#         result.append(i)
        
# result.sort(reverse=True)
# print(result)

# for j in result:
#     if j in orders:
#         orders.count(j)
#         print(orders.count(j))

#----------- 
#함수

# def abc():
#     global aa,bb##내장함수 외에서도 적용시키기
#     aa=3
#     bb=5
#     print(aa,bb)

# abc()
# print(aa,bb)

#argement랑 parameter랑 개수 맞추기
# def getsum(a,b,c):
#     return a+b+c

# ret=getsum(4,6,7)
# print(ret)

# #deault parameter랑 개수 맞추기
# def getsum(a,b=6,c=7):#고정값(deault parameter)은 무조건 우측에!!!
#     return a+b+c

# ret=getsum(4)
# print(ret)

#패킹
# num=[1,2,3,4,5]
# num2=(1,2,3,4,5)
# print(num,num2)

# #언패킹

# a,b,c,d,e=num
# print(a,b,c,d,e)
# a,b,c,d,e=num2
# print(a,b,c,d,e)
# #언패킹시 남는값을 *을 사용하여 리스트에 담을수 있다.
# a,b,*c=num
# print(c)
# a,b,*c=num2
# print(c)

#map
#리스트나 튜플같은 순회가능한 데이터 구조 값들에 
#함수를 일관적으로 적용하고
#정용후 값을 map이라는 객체로 반환
#사용법 map(함수,iterebles)


# num=['1','2','3']
# lst1=[]
# for i in num:
#     lst1.append(int(i))
# print(lst1)

# #map 함수 이용시
# lst2=map(int,num)
# print(lst2)           #map 이라는 함수 객체를 반환
# print(list(lst2))     #리스트의 형태로 바꿔서 출력

# lst1=[1,2,3]
# lst2=[4,5,6]
# #lst3라는 리스트에 lst1과lst2


# a,b=map(int,input().split())
# print(f'두 숫자의 차는 {a-b} 입니다.')

# t에서 1씩 증가=5 6 7
# t에서 2씩 감소=5 3 1
# t=int(5)
# print('t에서 1씩 증가=%d %d %d' %(t,t+1,t+2))
# print(f't에서 2씩 감소={t} {t-2} {t-4}')


# a+b=9
# a-b=5

# a=7
# b=2
# c=('a+b=')


# print(f'{c}{a+b}')
# print(f'a-b={a-b}')

# a=int(input())
# if a>=10:
#     print('WOW')

# map(함수,iterablese)
# lst3=list(map(func.lst1,lst2))
# print(lst3)

#filter
#리스트나 튜플 같은 순화 가능한 데이터구조 값들을 함수에 적용하는데
#적용후 값중True만 반환 !! filter라는 객체로 반환

#리스트에서 짝수만
# num=[1,2,3,4,5,6,7,8,9]

# def get_even(t):
#     return eTru if t%2==0 else False
# result=filter(get_even,num)
# print(list(result))

#lambda
#익명함수,,함수를 간략하게 적기 위해서 사용!

#숫자 2개 입력받고 getsum 함수로 전달
#getsum 함수에서 전달받은 두수의 합을 리턴함
#리턴 받은 값 출력하기
#1
# def sum(a,b):
#     return a+b
# ret=sum(3,5)
# print(ret)
# #2
# result=(lambda a,b:a+b)(3,5)   
# print(result)
# #3 
# sum2=(lambda a,b:a+b)
# print(sum2(3,5))

# lst1=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
# #두 리스트 값들의 합을 lst3에 람다 함수를 사용하여 값을 채운 후 출력하기   map+lambda
# result=(lambda x,y:x+y)
# lst3=map(result,lst1,lst2)
# print(list(lst3))


# lst3=map(lambda x,y:x+y,lst1,lst2)
# print(list(lst3))

#리스트에서 짝수만 빼오기 filter,lambda
# lst=list(range(100))
# lst2=filter(lambda even:even%2==0,lst)
# print(list(lst2))  

#데이터에 일괄적용 =map
#데이터에 일괄적용하는데 True값만 따로 저장하겠다.=filter
#lambda 익명함수 (사용자 함수를 직접 적지 않고 간단하게 함수 사용하고 싶을때 사용)

#recursion  재귀!! 재귀호출
#함수가 하나 있는데 함수 자기가 자기자신을 계속 호출!
#1 2 3 4 5 6 7 8 9 10 10 9 8 7 6 5 4 3 2 1 
# for i in range(1,11):
#     print(i,end=' ')
# for i in range(10,0,-1):
#     print(i,end=' ')


# def abc(level):
#     if level==1:
#         return
#     print(level,end=' ')
#     abc(level+1)
#     print(level,end=' ')

# st= 'apple,banana,mango'
# #문자'a'가 존재 하는지 확인하고자 합니다
# index=st.find('a',8)
# print(index)   #없는 값은 -1값 반환\

# alpha=st.index('e')
# print(alpha)


# #대소문자 확인!
# st= 'apple,banana,mango'
# print(st.isupper())
# print(st.islower())
# print(st.isalpha())

# print(st.count('a'))# 문자열의 개수를 구할때


# #join(합치지) 나중 split의 반대개념
# st=['a','p','p','l','e']
# str2="".join(st)    #안에는 구분자를 넣습니다.
# print(str2)

# #리스트안에 문자를 합치는데 사이사이에 , 를 넣어라\
# str2=",".join(st)
# print(str2)

# st=['apple','banana','mango']
# str3=','.join(st)
# print(str3)

# st='apple,banana,mango'
# str2=st.upper()
# print(str2)
# str2=st.islower()
# print(str2)

# #공백지우기 
# st= '  apple  '
# str2=st.lstrip()   #오른쪽은 rstrip
# print(str2)


# #교체 replace
# str2=st.replace('ap','mp')
# print(str2)

# #리스트 값 추가
# st=['apple','banana','mango']
# st.append('orange')
# st.insert(1,'orange')  #리스트 값을 중간 또는 맨 아에 추가할때 사용
# print(st)

# st=[1,2,3]
# str=[4,5]
# st.append(str)
# print(st)

# st=[1,2,3]
# str=[4,5]
# st.extend(str)
# print(st)

#리스트 값 지우기
# st=[1,2,3]
# st.pop()
# print(st)

# st=[1,3,4,5,2,3,6,1]
# st.remove(4)
# print(st)

# st=[1,3,4,5,2,3,6,1]
# del st[3:]
# print(st)

# st=[1,3,4,5,2,3,6,3]
# st.reverse()
# print(st)
# st=[1,3,4,5,2,3,6,3]
# print(st[::-1])


#sort
# a1=[6,3,9]
# print(a1)
# a1.sort()  #오름차순 디폴트
# print(a1)
# a1=[6,3,9]
# a1.sort(reverse=True)
# print(a1)

# a1=[6,3,9]
# ret=sorted(a1)  #원본 데이터 값 유지 (sort 다른점)
# print(a1,ret)
# ret=sorted(a1,reverse=True)
# print(ret)

#lamda를 이용한 sort
# lst= list(range(10))
# # print(lst)
# # ret= sorted(lst,key=lambda x:x)
# ret=sorted(lst,key=lambda x:x,reverse=True)#내림차순 (문자건 숫자건 다 잘 작동)
# print(ret)
# ret=sorted(lst,key=lambda x:-x)#내림차순!  

# lst=[(3,'banana'),(2,'apple'),(1,'carrot')]
# ret=sorted(lst,key=lambda x:x[0])
# print(ret)

#딕셔너리
# st={'kevin':1,'john':2,'bob':3}

# # st['kate']='hi'#딕셔너리 (key랑value)추가하기
# # print(st)
# # st['kevin']=11
# # print(st)
# # del st ['kate']
# # print(st)
# lst=st.keys()
# print(list(st))

# lst=st.values()
# print(list(lst))

# lst=st.items()
# print(list(lst))

#딕셔너리 값 출력하기
# st={'kevin':1,'john':2,'bob':[1,2,3]}
# print(st.get('kevin','값 없음 없다구요'))

# #딕셔너리 값 정렬하기 
# st={'kevin':12,'john':27,'bob':35}
# #아이들의 나이가 적은순으로(오름차순으로)
# ret=dict(sorted(st.items(),key=lambda x:x[1]))
# print(ret)

#깊은 복사
# import copy
# lst=[[1,2],[3,4]]
# lst2=copy.deepcopy(lst)
# lst[0][0]=100
# print(lst[0][0])

#주소 값을 찍어보자
# a=5
# b=5
# print(id(a),id(b))

# lst=[1,2,3]
# lst2=lst
# print(id(lst),id(lst2))
# #얕은복사
# lst=[1,2,3]
# lst2=lst[:]
# print(id(lst),id(lst2))

# lst=[[1,2],[3,4]]
# lst2=lst[:]
# print(id(lst),id(lst2))
# print(id(lst[0]),id(lst2[0]))

# #깊은 복사
# import copy
# lst=[[1,2],[3,4]]
# lst2=copy.deepcopy(lst)
# print(id(lst[0]),id(lst[0]))

#zip 각각 묵어줌
# name_lst = ['신동민', '서재현', '박영서', '이태성', '정예원', '이은석']
# age_list = [17, 18, 22, 24, 25, 19]

# for name,age in zip(name_lst,age_list):
#     print(name,age)

# #lambda 매겨변수: 매개변수를 이용한 리턴값
# print((lambda x: x *x)(4))

# def pow(x):
#     return x *x


# 숫자 2개(아이디, 비밀번호)를 입력 받아주세요
# 아이디는 1111, 비밀번호는 2222를 입력해야 로그인 처리가 완료됩니다.
# 만약 아이디가 틀렸으면 "아이디가 틀렸습니다" 출력
# 만약 아이디는 맞지만, 비밀번호가 틀렸으면 "비밀번호가 틀렸습니다" 출력
# 만약 아이디와 비밀번호가 모두 맞으면 "로그인성공" 출력
# for i in range(4):
#     print(1,end='')
a=(1,2,3,4,5,)
for i in range(0,-1):
    print(i)
