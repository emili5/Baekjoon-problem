import sys
input=sys.stdin.readline
n,m=map(int,input().split())

pok=dict()

for i in range(1,n+1):
    a=input().rstrip()
    pok[i]=a
    pok[a]=i


for i in range(m):
    ans=input().rstrip()
    if ans.isdigit():
        print(pok[int(ans)])
    else:
        print(pok[ans])
