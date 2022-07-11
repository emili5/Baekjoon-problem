r,b=map(int,input().split())

for L in range(3,r+b+1):
    W = (r + b) // L
    if L*W==r+b and (L-2)*(W-2)==b:
        if L>=W:
            print(L,W)