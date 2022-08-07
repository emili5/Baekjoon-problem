import sys
input=sys.stdin.readline

def Count(dis):
    cnt=1
    cur=location[0] # 공유기가 설치된 이전 집 위치
    for i in range(1,len(location)):
        if location[i]-cur>=dis: # 현재 집에서 이전 집까지의 거리가 넘어온 거리보다 더 먼 집이면
            cnt+=1 # 공유기 설치
            cur=location[i] # 공유기 설치된 이전 집 갱신
    return cnt


n,c=map(int,input().split()) 

location=[int(input().rstrip()) for _ in range(n)]

location.sort()
lt=1
rt=location[-1]-location[0]
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:# 설치해야 하는 공유기 수가 더 크면 
        res=mid
        lt=mid+1 #거리를 늘려줌
    else:
        rt=mid-1
print(res)
