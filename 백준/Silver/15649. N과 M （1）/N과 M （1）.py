#백트래킹
def backTracking():
    if len(s)==m: # 기저 조건
        print(*s)
        return
    for i in range(1,n+1):
        if not visited[i]:# 방문을 안했다면
            visited[i]=True #방문했다고 표시하고
            s.append(i) # 값 넣음
            backTracking() # 다시 백트래킹 함수 반복
            s.pop() #함수를 빠져나왔다면 기저조건을 만족한 것이므로 해당 값을 빼고 
            visited[i]=False # 다시 그 방문안함으로 바꿔줌-> 안바꿔주면 다음 탐색을 할 수가 없음

n,m=map(int,input().split())
s=[] #출력 수열 넣을 리스트(stack)
visited=[False]*(n+1) # 특정 수를 셌는지 아닌지 확인하는 배열!!!
backTracking()