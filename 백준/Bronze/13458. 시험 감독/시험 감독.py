import sys
input=sys.stdin.readline
n=int(input())
per=list(map(int,input().split()))
b,c=map(int,input().split())

cnt=n
for i in range(n):
    per[i]-=b
    if per[i]>0:
        if per[i]%c==0:
            cnt+=per[i]//c
        else:
            cnt+=per[i]//c+1
print(cnt)