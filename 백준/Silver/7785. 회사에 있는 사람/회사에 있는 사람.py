import sys

n=int(sys.stdin.readline())
stat=set()
for _ in range(n):
    a,b=input().split()
    if b=='enter':
        stat.add(a)
    else:
        stat.remove(a)

for i in sorted(stat,reverse=True):
    print(i)
