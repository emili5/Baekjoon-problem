import sys
input=sys.stdin.readline
n=int(input())

#한 중 띄어쓰기 입력을 받을 때에는 이렇게 받기
arr=set(map(int,input().split()))
arr=list(arr)
arr.sort()

for i in arr:
    print(i,end=' ')