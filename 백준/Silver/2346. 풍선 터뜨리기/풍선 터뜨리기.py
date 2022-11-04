import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
q = deque(enumerate(map(int, input().split())))
res=[]

while q:
    idx,term=q.popleft()
    res.append(idx+1)

    if term>0:
        q.rotate(-(term-1))
    elif term<0:
        q.rotate(-term)

print(*res)
        
