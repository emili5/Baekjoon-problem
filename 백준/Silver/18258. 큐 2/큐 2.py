import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
q=deque()

for _ in range(n):
    dir=input().rstrip()
    if " " in dir:
        word,num=map(str,dir.split())
        num=int(num)
        q.append(num)
    else:

        if q:
            if dir=="front":
                print(q[0])
            elif dir=="back":
                print(q[-1])
            elif dir=="pop":
                print(q.popleft())
            elif dir=="empty":
                print(0)
            elif dir=="size":
                print(len(q))
        else:
            if dir=="empty":
                print(1)
            elif dir=="size":
                print(0)
            else:
                print(-1)
            