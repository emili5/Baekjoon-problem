import sys
input=sys.stdin.readline

n,m=map(int,input().split())

answer=0
S=[]
check=[]

for _ in range(n):
    S.append(input().rstrip())
for _ in range(m):
    check.append(input().rstrip())

for i in range(m):
    if check[i] in S:
        answer+=1
print(answer)