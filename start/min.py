# MINCODING
# APPLE
# SKTOWN
#출력  GEN
# a=input()[-1]
# b=input()[-1]
# c=input()[-1]
# d=a+b+c
# print(d)

#===
# import sys
# sys.stdin = open("input.txt", "r")

# 1.문자열 입력 받고 출력해서 확인해보기
# st = 'hello'

# 1.주어지는 입력값은 아래와 같음
# hello

# 1.아래에 정답을 입력하시오
# st='hello'
# print(st)


# 2.정수형 변수 입력 받고 출력해서 확인해보기
# N = 45
# A, B, C = 1, 2, 3

# 2.주어지는 입력값은 아래와 같음
# 45
# 1 2 3

# 2.아래에 정답을 입력하시오
# N=input()
# A,B,C=map(int,input().split())
# print(N)
# print(A,B,C)


# 3.실수형 변수 입력 받고 출력해서 값이 잘 들어갔지 확인해보기
# F = 3.14
# A, B, C = 1.2, 2.3, 3.4

# 3.주어지는 입력값은 아래와 같음
# 3.14
# 1.2 2.3 3.4

# 3.아래에 정답을 입력하시오
# F=float(input())
# A,B,C=map(float,input().split())
# print(F)
# print(A,B,C)


# 4.한 줄에 있는 공백으로 구분된 단어들을 각각 문자열로 리스트에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# lst = ['one', 'two', 'three']

# 4. 주어지는 입력값은 아래와 같음
# one two three

# 4.아래에 정답을 입력하시오
# a=list(input().split())
# print(a)


# 5.한 줄에 있는 공백으로 구분된 숫자들을 각각 숫자로 리스트에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# (map 함수를 이용하여 문자열을 숫자로 바꾼 후 리스트로 변환)
# lst = [1, 2, 45, 43]

# 5. 주어지는 입력값은 아래와 같음
# 1 2 45 43

# 5.아래에 정답을 입력하시오
# lst=map(int,input().split())
# print(*lst)


# 6.한 줄에 있는 공백없는 한자리 숫자들을 각각 숫자로 리스트에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# lst = [1, 2, 3, 4]

# 6. 주어지는 입력값은 아래와 같음
# 1234

# 6.아래에 정답을 입력하시오
# lst=((input()))
# print(list(lst))


# 7.2차원 (N*N) 공백없는 한자리 숫자들을 2차원 arr에 저장하고 출력해서 값이 잘 들어갔지 확인해보기
# N=4
# lst=[[1,0,1,1],[1,0,0,1],[0,0,0,1],[1,0,0,0]]

# 7. 주어지는 입력값은 아래와 같음
# 4
# 1011
# 1001
# 0001
# 1000

# 7.아래에 정답을 입력하시오
# N=input()
# lst=list(input().split())
# print(N)
# print(lst)



# 8.2차원 (N*N) 정수값을 2차원 arr에 저장하고 출력해서 값이 잘 들어갔지 확인해보기 (N값과 arr값)
# N=4
# arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# 8. 주어지는 입력값은 아래와 같음
# 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16

# 8.아래에 정답을 입력하시오



# 9.(입력값 없음) 0값 10개를 가진 1차원 lst 생성 후 출력해서 값이 잘 들어갔지 확인해보기
# lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# 9.아래에 정답을 입력하시오

# 10.(입력값 없음) 0값 3 * 3 개를 가진 2차원 arr생성 후 출력해서 값이 잘 들어갔지 확인해보기
# arr = [[0, 0, 0],
#        [0, 0, 0],
#        [0, 0, 0]]

# 10.아래에 정답을 입력하시오



# print('수고하셨습니다.')

#2번
# a=list('ABKTKFCFBBQQTPZF')
# b,c=input().split()
# result=0
# for i in a:
#     if i==(b):
#         result+=1
#     if i==(c):
#         result+=1
# print(result)

#3번
# a=(input())
# b=int(input())
# print(f'{a[:b]}A{a[b:]}')

#4번
#입력:  3 4 1 2  5 3 8 9
#출력: 12 12 4 7

# a=input().split()
# b=input().split()
# result=[0,0,0,0]
# for i in range(0,4):
#     result[i]=(int(a[i])+int(b[3-i]))
# print(*result)

#5번
# a=input()
# b=int(input())
# print(f'{a[:b]}{a[b+1:]}')

#6번 
# a=(input().split())
# result=[a[0],0,0,0,0,0]
# for i in range(1,6):
#     result[i]=(int(a[i]))+(int(result[i-1]))
# print(*result)

#7번포기


#1번
# a,b,c=map(int,input().split())
# for j in range(c):

#     for i in range(a,b+1):
#         print(i,end=' ')
#     print()

#2번
# lst=[['A','B','C','D','E','F'],
# ['G','H','I','J','K','L'],
# ['M','N','O','P','Q','R']]
# A,B=map(int,input().split())
# for i in lst:
#     for j in range(A,B):
#         print(j)   
#     print()

# a,b,c=(input().split())
# # print(c)
# for i in range(int(b)):
#     for j in range(int(a)):
#         print(c*j)


# lst =[]
# for _ in range(3):
#     lst.append(input())

# a=input()
# b=input()
# c=input()
# d=a,b,c
# result=0
# for i in (d):
#     if 'M' in i:
#         result+=1

# if result>0:
#     print('M이 존재합니다')
# else:
#     print('M이 존재하지 않습니다')
#------------------------------------------
# ans = cnt =0
# for i in range(n):
#     if lst[i]==0:
#         cnt=0
#     else:
#         cnt+=1
#         if ans<cnt:
#             ans=cnt
# print(f'#{test_case},ans')


# a,b=(input().split())
# c=a,b

# lst=[['A','7','9','T','K','Q'],
# ['M','I','N','C','O','D']]

# result=''
# cnt=''
# for i in lst:
#     if a in i:continue
#     result+=a
# else:
#     cnt+=a
# print(f'{result} : 존재')
# print(f'{cnt} : 없음')
#사전순으로 가장뒷글자,가장앞글자 인덱스 번호

#  이 모양으로 땅을 갖을 수 있다고 할때 어느 땅을 갖어야 할까요?
#  2*3 배열만큼 잘라서 합을 구할떄 최대값은 몇 일까요? !!

#  ***
#  ***

# arr=[[1, 5, 4, 2],
#     [1, 3, 4, 2],
#     [3, 5, 3, 2],
#     [2, 6, 4, 1]]

# # for i in arr[:2]:
# #     for j in i[:3]:
# #         print(j,end=' ')
# #     print()

# def getsum(a,b):
#     sum=0
#     for i in range(2):
#         for j in range(3):
#             sum+=arr[a+i][b+j]    #범위
#     return sum
# maxv=-21e8
# for i in range(3):
#     for j in range(2):
#         ret=getsum(i,j)              #최대값 위치
#         if ret>maxv:
#             maxv=ret
# print(maxv)

#==========================파이참202302026=========================================================
# arr = [[3, 5, 4],
#        [1, 1, 2],
#        [1, 3, 9]]
#
# directy=[-1,1,0,0]
# directx=[0,0,-1,1]
#
# y,x=map(int,input().split())
# sum=0
# for i in range(4):
#     dy=y+directy[i]
#     dx=x+directy[i]
#     if 0<=dy<3 and 0<=dx<3:
#         sum+=arr[dy][dx]
# print(sum)

#좌표값 하나 입력 받아주세요
#입력받은 좌표로 부터 대각선에 있는곳의
#값들의 곱을 구해서 출력 해주세요!!
# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
# 위 아래 좌 우로 2칸까지 떨어진 곳들의 합을 구하기
# 2 2 입력시  18 출력
# (9+9=18)
#
# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# y, x = map(int,input().split())
#
# movey = [-1, 0, 1, 0]
# movex = [0, 1, 0, -1]
#
# sum = 0
# for i in range(4):
#     for j in range(1,4):
#         newy = y + movey[i] * j
#         newx = x + movex[i] * j
#
#         if 0 <= newy <= 4 and 0 <= newx <= 4:
#             sum += arr[newy][newx]
#
# print(sum)

# arr=[[1,2,3,4],
#     [1,2,9,4],
#     [1,9,3,9],
#     [1,2,9,4]]

# #문제 위 아래 좌 우 좌표들의 합이 가장 큰곳의 합과 그 기준 좌표값을 출력하기
# def isSum(y,x):
#     directy=[-1,1,0,0]
#     directx=[0,0,-1,1]      #x,y= 상하좌우 값들의 좌표
#     sum=0
#     for i in range(4):      #4번 반복
#         dy=directy[i]+y
#         dx=directx[i]+x
#         if dy<0 or dx<0 or dy>3 or dx>3:continue   #이럴떄를 제외하고 함수계속실행
#         sum+=arr[dy][dx]
#     return sum

# Maxvaule=int(-21e8)
# Maxi=0
# Maxj=0
# for i in range(4):
#     for j in range(4):
#         ret=isSum(i,j)   #ret은 0,0 부터 끝까지
#         if ret>Maxvaule:        #만일 ret이 Maxvalue보다 크면
#             Maxvaule=ret        #Maxvaule는 ret 이됨
#             Maxi=i
#             Maxj=j
# print(Maxvaule,Maxi,Maxj)

# a,b,c=map(int,input().split())
# Max=0
# if a>=b and a>=c:
#     Max=a
#     print(f'MAX={Max}')
# elif b>=a and b>=c:
#     Max=b
#     print(print(f'MAX={Max}'))
# else:
#     print(f'MAX={c}')
    
# Min=0
# if a<=b and a<=c:
#     Min=a
#     print(f'MIN={Min}')
# elif b<=a and b<=c:
#     Min=b
#     print(print(f'MIN={Min}'))
# else:
#     print(f'MIN={c}')

# lst=list(map(int,input().split()))
# num=0
# for i in lst:
#     num+=1
#     if i>=70:
#         print(f'{num}번사람은{i}점PASS')
#     elif i>=50:
#         print(f'{num}번사람은{i}점RETEST')
#     elif i<50:
#         print(f'{num}번사람은{i}점FAIL')
# a=input()
# b=[1]*4

# for i in b: #0 1 2 3
#     for j in b:  # 0 1 2
#         print(j*a,end='')
#     print()        

    
# a=int(input())
# b=[0]*3

# for i in b:               #0 1
#     for j in range(3):
#         a+=1
#         print(a-1,end=' ')     # 3 4 5   #6 7 8
#     print()

# def BBQ():
#     if 0<a and a<5:
#         print('초기값')
#     elif 6<a and a<10:
#         print('중간값')
#     else:
#         print('알수없는값')
    

# a=int(input())
# if a== 3 or 5 or 7:
#     for i in range(1,11):
#         print(i,end='')
# elif a== 0 or 8:
#     for j in range(10,0,-1):
#         print(j,end='')
# else:
#     BBQ()
# n=int(input())
# arr=[list(map(int,input())) for _ in range(n)]
# for i in range(n):
#     print=(arr[i])


# #리스트에 n개의 정수를 입력
# lst=list(map(int,input()))
# #타겟에 정수 1개 입력
# target=int(input())
# #타겟이 리스트 안에 있는지 존재 여부 출력
# for i in lst:
#     if target in i:
#         print('없음')
#     else:
#         print('없음')



#===================



# 베터리가 몇% 충정 되어 있는지 O(n)보다 빠르게 검색해서 알려주세요

# bettery='######____'

# def parametric_search(st,ed):
#     Max=-1
#     while 1:
#         mid=(st+ed)//2
#         if bettery[mid]=='_':
#             ed=mid-1
#         elif bettery[mid]=='#':
#             Max=mid
#             st=mid+1
#         if st>ed:
#             break
#     return Max+1

# answer=parametric_search(0,9)
# print(answer*10)

#=======================================
# 워드 작업 중 정전으로 인하여 컴퓨터가 강제 종료 되었습니다.
# 다시 전기가 들어와 컴퓨터를 켰더니 다행이도 자동복구가 실행 되었습니다.
# 우리는 자동복구가 되었을떄 커서의 위치가 어디인지를 알려줘야 합니다.
# 커서의 위치를 알려주는 프로그램을 완성해 주세요.
# 시간복잡도 O(n^2) 보다 빨라야 합니다.

# 6*12 size 리스트 입니다.

# curser=[ 
#  '##########',
#  '##########',
#  '###_______',
#  '__________',
#  '__________',
#  '__________',
# ]

# st=0
# ed=len(curser)
# mid=(st+ed)//2

# if curser[mid] not in '#':
#     ed=mid-1
# if curser[mid] in '#':
#======20230207

# a=[['B','D','5','Q','A'],['Q','E','R','E','F']]
# rlt=input()

# if rlt.islower():
#     for i in a[0]:
#         print(i,end='')
# if rlt.isupper():
#     for i in a[1]:
#         print(i,end='')
# if rlt.isdigit():
#     print("HGFEDCBA")


# arr=[[4,3,1,1],
# [3,1,2,1],
# [0,0,1,2]]

# a=int(input())
# sum=0
# for i in arr:
#     sum+=(i.count(a))
# print(f'{sum}개 존재합니다')



# a=list(map(int,input().split()))
# b=(a.index(7))     #인덱스 자리
#      #역배열
# c=(a[-1:b-1:-1])   
# for i in c:
#     print(i,end=' ')

# num=int(input())


# a=list(map(int,input().split()))
# Max=0
# Min=a[0]
# for i in a:
#     if i>Max:
#         Max=i
# for j in a:
#     if j<Min:
#         Min=j
# print(f'{Max-Min}')

# a=[4,3,6,1,3,1,5,3]
# b=int(input())
# c=a.count(b)
# print(f'숫자{b}개수는{c}개')

# a=[['A','B','C','D','E'],
# ['E','A','B','A','B'],
# ['A','C','D','E','R']]

# b=input()
# print(b)
# c=a.count(b)
# print(c)

# a=['A','F','G','A','B','C']

# b,c=input().split()
# count=0
# for i in a:
#     # if i in b or c:
#     #     count+=1
#     if i in b:
#         count+=1
#         if b =='A':
#             count-=0.5
#     if i in c:
#         count+=1
#         if c =='A':
#             count-=0.5
   
# if count==2:
#     print(f'와{int(count)}개')
# elif count==1:
#     print(f'오{int(count)}개')
# elif count==0:
#     print(f'우{int(count)}개')

# a=[3,4,2,5,7,9]
# b,c=map(int,input().split())
# a[b],a[c]=a[c],a[b]
# for i in a:
#     print(i,end=' ')
#------------------20230208-----------------
# a=[[0]*4 for _ in range(3)]
# b=int(input())
# for i in range(3):
#     for j in range(4):
#         b+=1
#         a[i][j]=b
# for rlt in a:
#     print(rlt)

# arr=[3,4,5,1,6,9]
#
# def abc(level,sum):
#     print(sum,end=' ')
#     if level==5:
#         return
#     abc(level+1,sum+arr[level+1])
#
# abc(0,arr[0])
# a,b=map(int,input().split())
# lst=list(map(int,input().split()))

# Max=-21e8
# Min=21e8
# # for i in range(a-b+1):
# #     if lst[i:b+i]>Max:
# #         Max=lst[i:b+i]
# # print(Max-Min)  


# for i in range(a-b+1):
#     sum=0
#     for j in lst[i:b+i]:
#         sum+=j

#     if sum>Max:
#         Max=sum
#     if sum<Min:
#         Min=sum

# print(Max-Min)
    

#------





# T=int(input())
# for t in range(T):   
#     a,b=map(int,input().split())
#     lst=list(map(int,input().split()))
#     Max=-21e8
#     Min=21e8

#     for i in range(a-b+1):
#         sum=0
#         for j in lst[i:b+i]:
#             sum+=j
#         if sum>Max:
#             Max=sum
#         if sum<Min:
#             Min=sum
#     print(f'#{t} {Max-Min}')

# a=int(input())
# card=list(map(int,input()))
# df=[]
# for i in card:
#     if i
    
# ===========================20230209
#
# # 5
# # 49679    9  2
# # 5
# # 08271   8 1
# # 10 
# # 7797946543    7  3 
# N=int(input())   #카드개수
# card=list(map(int,input())) #카드
# num=[0]*10   #빈배열 0~9 

# for i in card:          #카드숫자를i에 넣어줌
#     num[i]+=1              #넘에+1을 해준다 카드위치찾기위해서

# Max=0            #최대값    max가 4가되어버림
# Maxnum=0          #최대값숫자
# for j in range(10):           
#     if num[j]>=Max:        #배열의 최대값구해하기
#         Max=num[j]            #2개 000
#         Maxnum=(j)
# print(Maxnum,Max)


# # print(f'{}{Max}')    

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# # for test_case in range(1, T + 1):
# #     n=int(input())          #가로길이     9
# #     box=list(map(int,input().split()))
# #     max=0
# #     for i in range(n):#012345678
# #         sum=0
# #         for j in range(n):#012345678
# #             if box[i]>=box[j+i]:
# #                 #00 01 02 03 04 05 06 07 08
# #                 #11 12 13 14 15 16 17 18

# K=한번충전으로 최대 이동 정류장수
# M=충전기가 설치된 정류장 번호
# N=목적지    
#input    
# K N  M
# 3 10 5    # 
# 1 3 5 7 9        3

# 3 10 5
# 1 3 7 8 9        0  

# 5 20 5
# 4 7 9 14 17      4
#A= 한번충전으로 최대 이동 정류장수
#B= 목적지

#C= 충전기 개수

# =======전기버스===================
# a,b,c=map(int,input().split())  #3 10 5
# char=list(map(int,input().split()))  
# #(1 3 5 7 9)충전기 설치 정류장번호

# line=[0]*(b+1)    #목적지 개수만큼 리스트만듬
# for i in char:
#     line[i]+=a      #충전기 설치된 정류장번호에 최대이동 수를 넣음

# for j in range(0,(b+1),a):#출발지점부터 목적지 b까지 최대이동수 a를넣음
#     if line[j] in a:
#         pass
#     else:
#         print(0)
        
    
# #     print(j)
# # print(line)
#=======================================20230210=====================
#버블정렬
# arr=[1,5,3,4,9,7,6,2]  #8
# n=len(arr)   
# for i in range(n-1,0,-1):  #7부터 1까지 -1씩 비교
#     #(7654321)
#     for j in range(i):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#------------------------------swea 색종이
# N=int(input())
# R1=map(int,input().split())
# R2=map(int,input().split())


# a=[[0]*10 for _ in range(10)]   #총범위 10x10
# N=int(input()) #칠할 영역 개수

# n,m=map(int,input().split())

# a=list(map(int,input().split()))  #1233

# b=[[0]*10 for _ in range(10)]

# for i in range(a[0],a[2]+1): #1234
#         for j in range(a[1],a[4]+1):  #234
#             b.append([i,j])
# print(b)

#--------------------------------minco
# a,b=map(int,input().split())
# c,d=map(int,input().split())

# arr=[[0]*3 for _ in range(3)]
# value='A'
# for i in range(3):
#     for j in range(3):
#         arr[i][j]=value
#         value=chr(ord(value)+1)

# arr[a][b],arr[c][d]=arr[c][d],arr[a][b]\


# T=int(input())
# for test_case in range(1,T+1):
#     n,m=map(int,input().split())  #5 1
#     lst=[[0]*n for _ in range(n)]   #빈배열 n곱하기n개만듬
#     nlst=[list(map(int,input().split()))for _ in range(m)]

#     for k in range(m):
#         for i in range(nlst[k][0],nlst[k][2]+1):
#             for j in range(nlst[k][1],nlst[k][3]+1):
#                 lst[i][j]+=1
#     rlt = 0
#     for x in lst:
#         for y in x:
#             if y>0:
#                 rlt+=1
#             if y>1:
#                 rlt+=2


#     print(f'#{test_case} {rlt}')
#========================================20230213==============================
#중복순열
	
# n=3
# dice=[1,2,3,4]
# path=['']*n     
# def abc(level):
#      if level==n:               #level 3일때 돌아가는거
#           for i in range(n):
#                print(path[i],end=' ')
#           print()
#           return
#      for i in range(4):
#         if i==1: continue
#         path[level]=dice[i]
       
#         abc(level+1)
#          #path[level] =' '
        

# abc(0)



# n=3
# card=['A','B','C','D']
# path=['']*n
# def abc(level,start):
#     # if level>0 and path[level-1]=='B': return
#     if level==n:
#         for i in range(n):
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(start,4):
#         path[level]=card[i]
#         # if path[level-1]==path[level]: return
#
#         abc(level+1,i+1)
#
# abc(0,0)


# n=3  #카드 3묶음
# card=['A','B','C','D'] #카드
# path=['']*n  #?
# # def abc(level):
# #     if level==n:  #레벨이 3이되면
# #         for i in range(n): #3번반복
# #             print(path[i],end=' ')
# #         print()
# #         return #..
# #     for i in range(4):
# #         path[level]=card[i]
# #         abc(level+1)
# #나는솔로
#        #A B C D E F
# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# a=input()  #문자 하나 입력받기
# rlt=[]
# for i in range(5):
#     for j in range(6):
#         if arr[i][j]==1:
#             rlt+=arr[j]
#         else:

# #arr 을 for문돌리면서 1을찾기
# #1의 좌표를 찾고 그좌표에서 같은 i값에 있는 것을 찾기
# #찾은걸 출력#같은i값에서찾은 j위치가 0이면a 1이면b 2이면c....
# #만약 같은 i값에 없으면 형제없음 출력

# # 문자를 하나 입력받아 주세요
# #그리고 입력받은 문자의 형제노드를 출력해주세요
# #예
# #A입력시 형제없음 출력됨
# #B입력시 C출력됨
# #E입력시 D출력됨
# #F입력시 형제없음이 출력됩니다

#========================================20230213==============================
#중복순열
	
# n=3
# dice=[1,2,3,4]
# path=['']*n     
# def abc(level):
#      if level==n:               #level 3일때 돌아가는거
#           for i in range(n):
#                print(path[i],end=' ')
#           print()
#           return
#      for i in range(4):
#         if i==1: continue
#         path[level]=dice[i]
       
#         abc(level+1)
#          #path[level] =' '
        

# abc(0)



# n=3
# card=['A','B','C','D']
# path=['']*n
# def abc(level,start):
#     # if level>0 and path[level-1]=='B': return
#     if level==n:
#         for i in range(n):
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(start,4):
#         path[level]=card[i]
#         # if path[level-1]==path[level]: return
#
#         abc(level+1,i+1)
#
# abc(0,0)


# n=3  #카드 3묶음
# card=['A','B','C','D'] #카드
# path=['']*n  #?
# # def abc(level):
# #     if level==n:  #레벨이 3이되면
# #         for i in range(n): #3번반복
# #             print(path[i],end=' ')
# #         print()
# #         return #..
# #     for i in range(4):
# #         path[level]=card[i]
# #         abc(level+1)
# #나는솔로
       #A B C D E F
# arr = [[0,1,1,0,0,0],
#        [0,0,0,1,1,0],
#        [0,0,0,0,0,1],
#        [0,0,0,0,0,0],
#        [0,0,0,0,0,0]]
# a=input()  #문자 하나 입력받기
# rlt=[]
# for i in range(5):
#     for j in range(6):
#         if arr[i][j]==1:
#             rlt+=arr[j]
#         else:

#arr 을 for문돌리면서 1을찾기
#1의 좌표를 찾고 그좌표에서 같은 i값에 있는 것을 찾기
#찾은걸 출력#같은i값에서찾은 j위치가 0이면a 1이면b 2이면c....
#만약 같은 i값에 없으면 형제없음 출력

# 문자를 하나 입력받아 주세요
#그리고 입력받은 문자의 형제노드를 출력해주세요
#예
#A입력시 형제없음 출력됨
#B입력시 C출력됨
#E입력시 D출력됨
#F입력시 형제없음이 출력됩니다

#==========================20230214
# name=['K','F','C','D','M','G','A']
# arr=[[0,1,1,1,0,0,0],
#     [0,0,0,0,1,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0]]
# path=[]
# def abc(now):
#     global path
#     path.append(name[now])
#     for i in range(len(name)):
#         if arr[now][i]==1:
#             abc(i)
# abc(0)
# print(*path)


#a->d까지 가는방법 경로탐색
# name=list(input().split())   # B A C D
# arr=[
#     [0,0,1,1],
#     [1,0,1,0],
#     [1,0,0,1],
#     [0,0,0,0]]
# used=[0]*4
# answer=0
# path=[]

# def dfs(now):
#     global answer
#     path.append(name[now])
#     if now==3:
#         answer+=1
#         print(*path)
#         return

#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             dfs(i)
#             used[i]=0
#             path.pop()

# used[1]=1
# dfs(1)
# print(answer)
#==========================================
# name=['K','F','C','D','M','G','A']

# arr=[
#     [0,1,1,1,0,0,0],
#     [0,0,0,0,1,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
# ]
# path=[]
# def dfs(now):
#     global path
#     path.append(name[now])    #NOW=0 1 4 5  PATH K F M G
#     for i in range(len(name)):
#         if arr[now][i]==1:
#             dfs(i)
# dfs(0)
# print(*path)
#===========================================
# TREE 모양이 아닌 그래프 dfs 1번씩 탐색 순서 출력하기
# name=list(input().split())  # B A C D
# arr=[[0,0,1,1],
#      [1,0,0,0],
#      [0,1,0,1],
#      [0,0,0,0]]

# used=[0]*4
# answer=[]

# def dfs(now):
#     global answer
#     answer.append(name[now])
#     for i in range(4):
#         if arr[now][i]==1:  # 인접행렬 탐색하다가 1체크가 되어 있으면
#             if used[i]==0:  # 한번도 방문한 적이 없으면
#                 used[i]=1   # 방문체크 해주고
#                 dfs(i)      # 들어가기

# used[0]=1   # 탐색 시작 인덱스에 1 체크하고
# dfs(0)      # dfs 탐색
# print(*answer)
#=======================
# name=list(input().split())  # B A C D
# arr=[[0,0,3,14],
#      [7,0,19,0],
#      [3,0,0,1],
#      [0,0,0,0]]
# used=[0]*4  # 방문 횟수 체크할라고
# Min=9999999999999999999

# #A에서 D까지 가는데 최소비용구하기
# def dfs(now,sum):
#     global Min
#     if now==3:
#         if sum<Min:
#             Min=sum        #최소sum구하기
#         return

#     for i in range(4):
#         if arr[now][i]>0:#이동할 수 있는 곳이라면
#             if used[i]==0:# 한번도 방문한 적이 없는 곳이라면
#                 used[i]=1
#                 dfs(i,sum+arr[now][i])   ###잘모르겠음
#                 used[i]=0
# used[1]=1            
# dfs(1,0)   #시작인덱스1//sum=0

# print(Min)
#=====================================
# name=list(input().split())  # A B C D E
# arr=[[0,4,0,0,0],
#     [0,0,1,2,9],
#     [5,0,0,7,0],
#     [0,0,0,0,1],
#     [0,0,0,0,0]]
# st=input()
# used=[0]*5
# cnt=0

# def dfs(now):
#     global cnt
#     # 도착점 E에 도착할때 마다 cnt+=1 해주기
#     if name[now]=='E': 
#         cnt+=1
#     # 인접행렬 탐색하는데...
#     for i in range(5):
#         # 이동 가능하며 한번도 방문한 적이 없다면
#         if arr[now][i]==1 and used[i]==0: 
#             # 방문체크 해주고
#             used[i]=1
#             dfs(i)
#             # 방문체크 해제 하기
#             used[i]=0
            

# # 입력받은 시작점의 인덱스 찾기
# st_index=0
# for i in range(5):
#     if name[i]==st:
#         st_index=i
#         break
# # 방문배열에 1 체크 후 dfs 시작하기
# used[st_index]=1
# dfs(st_index)
# print(cnt)
#=========================================================
# name=list(input().split())  # A B C D E
# arr=[[0,4,0,0,0],
#     [0,0,1,2,9],
#     [5,0,0,7,0],
#     [0,0,0,0,1],
#     [0,0,0,0,0]]
# used=[0]*5
# min=999999

# def abc(now,sum):
#     global Min
#     if now==4:
#         if sum<min:
#             min=sum
#         return
    
#     for i in range(5):
#         if arr[now][i]>0:
#             if used[i]==0:
#                 used[i]=1
#                 abc(i,sum+arr[now][i])
#                 used[i]=0



# used[0]=1
# abc(0,0)
# print(min)


#==============================20230214진도 이후 복습=======
# name=['K','F','C','D','M','G','A']

# arr=[
#     [0,1,1,1,0,0,0],
#     [0,0,0,0,1,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
# ]
# path=[]    #[1]정답을 입력받을 path를 만들기
# def abc(now):  #[3]now에 0을 넣기
#     global path  #[4]path는 글로벌로 받기
#     path.append(name[now])   #[5]path에 추가한다 네임의[now]번쨰를
#     for i in range(len(name)):#[6]반복한다 이름의 길이만큼
#         if arr[now][i]==1:    #[7]반복해서 1이나오면
#             abc(i)              #[8]나온 1의값의 위치번호로 now를설정하고 다시호출
# abc(0) #[2]abc함수 호출
# print(path)
#=====================================================
# name=list(input().split())  # B A C D
# arr=[[0,0,1,1],
#      [1,0,0,0],
#      [0,1,0,1],
#      [0,0,0,0]]

# path=[]   #[1]정답입력칸만들기
# used=[0]*4   #[2]방문횟수 체크를 위해 USED만들기
# def abc(now): #[4]NOW에 0을 처음에 넣음
#     global path 
#     path.append(name[now]) #[5]PATH에 처음NAME[NOW]를 추가
#     for i in range(4):      #[6]4번 반복함
#         if arr[now][i]==1:  #만약 1이체크되어있으면
#             if used[i]==0:  #그안에서 만약 USED에 방문기록이 없다면
#                 used[i]=1   #방문체크를 해줌
#                 abc(i)      #바로다음은 abc(2)호출

# used[0]=1
# abc(0)   #[3]ABC호출
# print(*path)
#=======================================
# # 한 지점에서 다른 지점까지 갈 수 있는 경로가 몇가지 인지 출력해 주세요 ( A -> D)
# name=list(input().split())   # B A C D
# arr=[
#     [0,0,1,1],
#     [1,0,1,0],
#     [1,0,0,1],
#     [0,0,0,0]]
# used=[0]*4
# answer=0  #경로가 몇가지인지 출력이니까
# def abc(now):
#     global answer
#     if now == 3:
#         answer+=1
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             abc(i)
#             used[i]=0
#
# used[1]=1
# abc(1)
# print(answer)


#==========================
# name=list(input().split())   # B A C D
# arr=[[0,0,3,14],
#     [7,0,19,0],
#     [3,0,0,1],
#     [0,0,0,0]]

# # A 에서 D 까지 가는 데 최소비용을 구하기
# used=[0]*4
# Min=999999999999999999999999
# sum=0
# def dfs(now):
#     global Min,sum
#     if now==3:
#         if sum<Min:     # 최소sum 구하기
#             Min=sum
#         return
#     for i in range(4):
#         if arr[now][i]>0: #이동할 수 있는 곳이라면
#             if used[i]==0: # 한번도 방문한 적이 없는 곳이라면
#                 used[i]=1
#                 sum+=arr[now][i]
#                 dfs(i)
#                 used[i]=0
#                 sum-=arr[now][i]

# used[1]=1
# dfs(1)     # 시작인덱스1 // sum=0
# print(Min)
#===========================================
# lst=list(map(int,input().split()))

# arr=[[0]*3 for _ in range(2)]



# for i in range(2):
#     for j in range(3):
#         for x in range(6):
#             arr[i][j]=lst[x]
# print(arr)
        
#==================

# name=['Chloe','Diane','Bob','Amym','Edger']
# arr=[[0,0,1,0,0],
#     [0,0,1,0,0],
#     [0,0,0,1,0],
#     [0,0,0,0,1],
#     [0,0,0,0,0]]

# maxv=0
# for i in range(5):
#     sum=0
#     for j in range(5):
#         if arr[i][j]==1:
#             sum+=1
#         if sum>maxv:
#             maxv=sum
#=====================================
# people = ['Amy','Bob','Chloe','Diane','Edger']

# arr = [[0,0,1,0,1],
#        [1,0,0,0,0],
#        [0,1,0,0,0],
#        [0,1,0,0,0],
#        [0,0,0,1,0]]

# # 여기서  가장 인기가 많은 사람은 누구인지 출력
# maxV=0
# for j in range(5):
#     sum = 0
#     for i in range(5):
#         if arr[i][j] == 1:
#             sum += 1
#     if maxV < sum:
#         maxV = sum
#         pp = people[j]
# print(pp)
#=========================
# # n,m=map(int,input().split())
# #65~82
# arr=[[0]*3 for _ in range(6)]
# for x in range(82,64,-1):
    
# for i in range(2,-1,-1):
#     for j in range(5,-1,-1):
        
#         arr[j][i]==chr(x)
# print(arr)

#============================20230215===========================
arr=[[3,5,9,6],
     [7,-8,1,6],
     [-10,2,3,9],
     [5,1,2,8],
     [4,7,1,8]]
cnt=0
def dfs(now,level,sum):
     global cnt
     if level==5:
          if sum>30:
               cnt+=1
          return
     for i in range(3):
         direct=[-1,0,1]
         dy=level
         dx=now+direct[i]
         if dx<0 or dx>3: continue
         dfs(dx,level+1,sum+arr[dy][dx])

for i in range(4):
     dfs(i,1,arr[0][i])     #now level sum
print(cnt)



# arr=[[4,5,2],
#     [-2,1,6],
#     [3,9,-4],
#     [3,5,2]]

# cnt=0
# def abc(level,sum):
#     global cnt
#     if level==4:
#         if sum>20:    ##
#             cnt+=1    ##
#         return
#     for i in range(3):
#         abc(level+1,sum+arr[level][i])  ###
# abc(0,0)
# print(cnt)