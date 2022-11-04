import sys

input=sys.stdin.readline


n=int(input())

dic={}

for _ in range(n):
    name=input().rstrip()
    if name in dic:
        dic[name]+=1
    else:
        dic[name]=1

best=max(dic.values())

res=[]
for k,v in dic.items():
    if v==best:
        res.append(k)
res.sort()
print(res[0])


