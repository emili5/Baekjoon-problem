import sys
import heapq
input=sys.stdin.readline
n=int(input())

h=heapq
arr=[]
for _ in range(n):
    num=int(input())
    if num==0:
        if len(arr)==0:
            print(0)
        else:
            print(-h.heappop(arr))
    else:
        h.heappush(arr,-num)