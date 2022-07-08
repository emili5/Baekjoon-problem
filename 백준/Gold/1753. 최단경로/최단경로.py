#자신의 점에서 다른 모든 정점으로의 최단경로를 구하는 다익스트라 알고리즘
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)


n,m=map(int,input().split())
s=int(input())
graph=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c)) # 노드의 거리와 노드번호 저장


#다익스트라 알고리즘 수행
def dijkstra(s):
    q=[]
    heapq.heappush(q,(0,s)) #처음에는 시작노드
    dis[s]=0
    # 가장 최단 거리가 짧은 거리 노드 꺼내기
    while q:
        dist,now=heapq.heappop(q)

        if dis[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost <dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(s)

for i in range(1,n+1):
    if dis[i]==INF:
        print('INF')
    else:
        print(dis[i])
