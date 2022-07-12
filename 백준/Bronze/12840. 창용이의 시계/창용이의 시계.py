import sys
input=sys.stdin.readline

MIN=60
HOUR=60*MIN
DAY=24*HOUR

h,m,s=map(int,input().split())
q=int(input())

#계산의 편리함을 위해 시간, 분을 다 초로 만들어주기
t=h*HOUR+m*MIN+s

# 초를 시간, 분 ,초로 바꿔주는 함수
def time(t):
    h=t//HOUR
    t%=HOUR
    m=t//MIN
    t%=MIN
    s=t
    return h,m,s

def change(c):
    global t
    t=(t+c)%DAY
for _ in range(q):
    ans=list(map(int,input().split()))
    if ans[0]==1:
        change(ans[1])
    elif ans[0]==2:
        change(-ans[1])
    else:
        h,m,s=time(t)
        print(h,m,s)