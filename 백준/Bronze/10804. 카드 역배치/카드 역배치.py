arr=[i for i in range(1,20+1)]
for _ in range(10):
    n,m=map(int,input().split())
    temp=arr[n-1:m]
    arr[n-1:m]=temp[::-1]
for i in arr:
    print(i,end=" ")
