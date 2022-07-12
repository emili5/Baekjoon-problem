import sys
input=sys.stdin.readline

while True:
    ans = 'yes'
    sen=input().rstrip()
    stack = []
    if sen=='.':
        break
    for i in sen:
        if i=='(' or i=='[':
            stack.append(i)
        else:
            if i==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                else:
                    ans='no'
                    break
            elif i==']':
                if len(stack)!=0 and stack[-1]=='[':
                    stack.pop()
                else:
                    ans='no'
                    break
    if len(stack)>0:
        ans='no'
    print(ans)
