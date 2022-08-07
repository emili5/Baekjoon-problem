def binary_search(arr,tar,s,e):
    while s<=e:
        m=(s+e)//2
        if arr[m]==tar:
            return m
        elif tar<arr[m]:
            e=m-1
        else:
            s=m+1
    return None


n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))


for i in b:
    if binary_search(a,i,0,n-1)!=None:
        print(1)
    else:
        print(0)

