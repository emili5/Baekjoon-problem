import sys
input=sys.stdin.readline

n=int(input())
s=set()
for _ in range(n):
    ans=input().split()
    
    #cmd 1개 일때
    if len(ans)==1:
        cmd=ans[0]
    #cmd val로 값이 2개 일때
    else:
        cmd,val=ans[0],ans[1]
        val=int(val)

    if cmd=='add':
        s.add(val)
    elif cmd=='remove':
        s.discard(val)
    elif cmd=='toggle':
        if val in s:
            s.discard(val)
        else:
            s.add(val)
    elif cmd== 'all':
        s = set([i for i in range(1, 21)])
    elif cmd == 'empty':
        s.clear()
    else:
        if val in s:
            print(1)
        else:
            print(0)
