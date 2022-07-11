import sys
input=sys.stdin.readline
n=input().rstrip()
digit=list(int(i) for i in n)
digit.sort(reverse=True)

if sum(digit)%3==0 and 0 in digit:
    print(*digit,sep='')
else:
    print(-1)
