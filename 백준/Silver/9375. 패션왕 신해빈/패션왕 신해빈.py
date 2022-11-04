import sys

input=sys.stdin.readline


n=int(input())


for _ in range(n):
    dic={}
    res=1
    m=int(input())
    for _ in range(m):
        a,b=map(str,input().split())
        if b in dic:
            dic[b]+=1
        else:
            dic[b]=1
    for k,v in dic.items():
        res*=(v+1)
    print(res-1)