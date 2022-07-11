import sys
from itertools import permutations
input=sys.stdin.readline
n=input().rstrip()
digit=list(int(i) for i in n)
digit.sort(reverse=True)
l=len(digit)
if sum(digit)%3==0 and 0 in digit:
    num=''.join(map(str,digit))
    print(int(num))
else:
    print(-1)
