import sys

input=sys.stdin.readline

n,m=map(int,input().split())

light=list(map(int,input().split()))

for _ in range(m):
    a,b,c=map(int,input().split())
    if a==1:
        light[b-1]=c
    elif a==2:
        for i in range(b-1,c-1+1):
            if light[i]==1:
                light[i]=0
            else:
                light[i]=1
    elif a==3:
        for i in range(b-1,c-1+1):
            light[i]=0
    else:
        for i in range(b-1,c-1+1):
            light[i]=1

for i in light:
    print(i,end=" ")

