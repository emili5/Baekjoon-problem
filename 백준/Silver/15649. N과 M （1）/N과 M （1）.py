from itertools import permutations
n,m=map(int,input().split())
arr=[]
for i in range(1,n+1):
    arr.append(i)
c=permutations(arr,m)
for i in c:
    for j in range(len(i)):
        print(i[j],end=" ")
    print()