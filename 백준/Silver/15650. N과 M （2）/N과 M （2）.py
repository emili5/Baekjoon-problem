def backTracking(start): #start변수를 넘겨주어 자기자신보다 큰 수가 다음에 들어올 수 있도록 함
    #기저조건
    if len(s)==m:
        print(*s)
        return

    for i in range(start,n+1):
        if i not in s:# 중복없이
            s.append(i)
            backTracking(i+1) # 자신 다음 수 백트래킹 
            s.pop()

n,m=map(int,input().split())
s=[]
backTracking(1)