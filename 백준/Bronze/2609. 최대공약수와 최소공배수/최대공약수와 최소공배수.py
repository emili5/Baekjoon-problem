import math

n,m=map(int,input().split())
G=math.gcd(n,m)
print(G)
print(n*m//G)
