import sys
input=sys.stdin.readline

n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    ans=[]
    t=a
    while True:
        if a%10 in ans:
            break
        ans.append(a%10)
        a*=t
    if a%10==0:
        res=10
    else:
        res=ans[b%len(ans)-1]
    print(res)
