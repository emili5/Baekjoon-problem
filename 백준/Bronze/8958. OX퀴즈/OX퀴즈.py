n=int(input())
v=[]
for _ in range(n):
    score = 0
    t = -1
    v=input()
    for i in v:
        if i=='O':
            t+=1
            score+=t+1
        else:
            t=-1
    print(score)