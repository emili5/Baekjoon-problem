from itertools import combinations
n,k=map(int,input().split())
arr=[int(input()) for _ in range(n)]
arr.sort(reverse=True)

cnt=0
for i in arr:
    if i<=k:
        cnt += k // i
        k %= i

print(cnt)