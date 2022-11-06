import sys

input=sys.stdin.readline

n=int(input())
time=[]
for _ in range(n):
    s,e=map(int,input().split())
    time.append((s,e))

time.sort(key=lambda x:(x[1],x[0]))

et=0 #진행할 회의 끝나는 시간 저장
cnt=0 # 회의 개수

for s,e in time:
    if s>=et:
        et=e
        cnt+=1
print(cnt)