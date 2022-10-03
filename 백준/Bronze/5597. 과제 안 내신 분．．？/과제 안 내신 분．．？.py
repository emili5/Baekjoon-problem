import sys

input=sys.stdin.readline

student=[int(input().rstrip()) for _ in range(28)]

check=[0]*(30+1)

for i in range(len(student)):
    check[student[i]]+=1

for i in range(1,len(check)):
    if not check[i]:
        print(i)



