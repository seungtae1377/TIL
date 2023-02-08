import sys
sys.stdin=open('input.txt', 'r')

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):

#     num=int(input())
#     a=list(map(int,input().split()))
#     Max=0
#     Min=a[0]
#     for i in a:
#         if i>Max:
#             Max=i
#     for j in a:
#         if j<Min:
#             Min=j
#     print(f'#{test_case} {Max-Min}')


# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):

#     Max=0
#     Min=a[0]
#     N,M=map(int,input())   #N은 정수의 개수 M은 범위 10 3
#     a=list(map(int,input().split()))
#     for i in a[:M]:
#         if Max<i:
#             Max=i

#         if i==(M-N):

#[0:4]    [1:5]   [2:6]  [3:7] [4:8][5:9][6:10][7:11]
#------------------20230208-------------------
# a,b=map(int,input().split())   #a는 총개수 b는 범위
# #a-b까지 b의 합을 출력
# #출력하면서 max값이랑 min값 만들고
# #123 더하고 234 더하고 345하는거?
# #max-min을 출력
# lst=map(int,input().split())
# def get_sum():   # 범위 값의 합을 구하는 함수
#     sum=0
#     for i in range(b):
#         sum+=lst[i]

#     return sum  
# Min=21e8
# Max=-21e8

# lst=list(map(int,input().split()))
# a,b=map(int,input().split())
# Max=-21e8
# Min=21e8
# for i in range(a):
#     if lst[i:b+i]>Max:
#         Max=lst[i:b+i]
# print(Max)  
#     if lst[i:b+i]<Min:
#         Min=lst[i:b+i]
# print(Max-Min)
# T=int(input())
# for t in range(T):
#     a,b=map(int,input().split())
#     lst=list(map(int,input().split()))

#     Max=-21e8
#     Min=21e8
#     # for i in range(a-b+1):
#     #     if lst[i:b+i]>Max:
#     #         Max=lst[i:b+i]
#     # print(Max-Min)  


#     for i in range(a-b+1):
#         sum=0
#         for j in lst[i:b+i]:
#             sum+=j

#         if sum>Max:
#             Max=sum
#         if sum<Min:
#             Min=sum

#     print(f'#{t} {Max-Min}')
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
#     print(f'#{t+1} {Max-Min}')

a=int(input())
card=list(map(int,input()))
print(a)
print(card)