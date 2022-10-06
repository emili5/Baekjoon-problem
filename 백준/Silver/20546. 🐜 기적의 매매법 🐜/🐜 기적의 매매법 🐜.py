import sys

input=sys.stdin.readline

money=int(input().rstrip())

price=list(map(int,input().split()))

n=len(price)

cntA,cntB=0,0
cashA,cashB=money,money

#A
for i in range(n):
    if cashA>=price[i]:
        cntA+=(cashA//price[i])
        cashA%=price[i]
    else:
        continue
#B
for i in range(n-3):
    if price[i]>price[i+1]>price[i+2]: #3일동안 가격이 계속 하락
        cntB+=(cashB//price[i+3]) #매수
        cashB%=price[i+3]
    elif price[i]<price[i+1]<price[i+2]:
        cashB+=(cntB*price[i+3])
        cntB=0
    else:
        continue


resultA=cashA+price[n-1]*cntA
resultB=cashB+price[n-1]*cntB

if resultA>resultB:
    print("BNP")
elif resultA<resultB:
    print("TIMING")
else:
    print("SAMESAME")
