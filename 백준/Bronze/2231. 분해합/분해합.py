N = int(input())
flag=0
for i in range(1, N+1):
    res=i
    k = i
    while i >=1:
        a = i % 10
        k += a
        i//=10
    if k == N:
        flag=1
        break
if flag:
    print(res)
else:
    print(0)
