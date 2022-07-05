a,b=input().split()
rev_a=a[::-1]
rev_b=b[::-1]
if int(rev_a)>int(rev_b):
    print(rev_a)
else:
    print(rev_b)

