import sys
input=sys.stdin.readline

n=int(input())
order=list(map(int,input().split()))

order.sort()

case=order[0]
per=order[0]

for i in range(1,n):
    per+=order[i]
    case+=per

print(case)
