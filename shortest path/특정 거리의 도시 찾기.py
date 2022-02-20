from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호 입력
n,m,k,x=map(int,input().split())
graph = [[] for _ in range(n+1)]

# 도로 정보 입력
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
dis=[-1]*(n+1)
# 가장 처음 도시는 거리 0으로 설정
dis[x]=0

# BFS로 최단 거리 탐색
q = deque([x])
while q:
    now = q.popleft()
    for next_city in graph[now]:
        # 아직 방문하지 않은 도시는
        if dis[next_city]== -1:
            # 현재 거리 + 1 -> 최단 거리 갱신
            dis[next_city]=dis[now]+1
            q.append(next_city)

# 최단거리가 k인 모든 도시 오름차순으로 출력
check = False
for i in range(1,n+1):
    #최단거리가 k인 도시가 존재하면 True로
    if dis[i] == k :
        print(i)
        check = True

#최단 거리가 k인 도시가 하나도 존재하지 않으면
if check == False:
    print(-1)




