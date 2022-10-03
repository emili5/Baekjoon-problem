import sys

input=sys.stdin.readline

n=int(input().rstrip())
m=int(input().rstrip())


G=[]

for i in range(n+1):
    G.append([])

for _ in range(m):
    i,j=map(int,input().split())
    G[i].append(j)
    G[j].append(i)

visited=[0]*(n+1)
cnt=0 #다녀간 정점 확인 변수

def dfs(G,v,visited):
    global cnt
    visited[v]=1

    for i in G[v]:
        if not visited[i]:
            dfs(G,i,visited)
            cnt+=1

dfs(G,1,visited)

print(cnt)