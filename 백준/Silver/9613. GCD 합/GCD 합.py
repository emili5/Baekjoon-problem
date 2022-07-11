from itertools import combinations
import math
n=int(input())
for _ in range(n):
    tot=0
    arr=(list(map(int,input().split())))
    c=combinations(arr[1:],2)
    for i in c:
        tot+=math.gcd(i[0],i[1])
    print(tot)