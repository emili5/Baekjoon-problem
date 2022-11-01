import sys
input=sys.stdin.readline

n=int(input())
info=[]
rank=[1]*n
for _ in range(n):
    w,h=map(int,input().split())
    info.append((w,h))

for i in range(n):
    for j in range(n):
        if info[i][0]<info[j][0] and info[i][1]<info[j][1]:
            rank[i]+=1
print(*rank)