import sys
from collections import deque
input=sys.stdin.readline

T=int(input())    
q=deque()

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    
    q.append([x,y])
    G[x][y]=0

    while q:
        
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            
            if 0<=nx<m and 0<=ny<n and G[nx][ny]==1:
                q.append([nx,ny])
                G[nx][ny]=0
                
    

for _ in range(T):
    m,n,k=map(int,input().split())
    G=[[0]*(n) for _ in range(m)]
    cnt=0
    for _ in range(k):
        i,j=map(int,input().split())
        G[i][j]=1
    
    for i in range(m):
        for j in range(n):
            if G[i][j]==1:
                   bfs(i,j)
                   cnt+=1
    print(cnt)        
   



