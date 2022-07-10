n=int(input())

arr=[input() for _ in range(n)]
stack=[]
for i in range(n):
    if arr[i]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif arr[i]=='size':
        print(len(stack))
    elif arr[i]=='empty':
        if len(stack)==0 :
            print(1)
        else:
            print(0)
    elif arr[i]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    else:
        k=int(arr[i].split(" ")[1])
        stack.append(k)
