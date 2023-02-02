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

a,b,c=(input().split())
# print(c)
for i in range(int(b)):
    for j in (a):
        print(c*j)
        
