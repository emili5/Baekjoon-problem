import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    one=set(map(int,input().split()))
    m=int(input())
    two=list(map(int,input().split()))
    for i in two:
        if i in one:
            print(1)
        else:
            print(0)
