import sys
sys.stdin=open('input.txt', 'r')

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    num=int(input())
    a=list(map(int,input().split()))
    Max=0
    Min=a[0]
    for i in a:
        if i>Max:
            Max=i
    for j in a:
        if j<Min:
            Min=j
    print(f'#{test_case} {Max-Min}')