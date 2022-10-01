import sys

input=sys.stdin.readline

password=['w','g','h','u','v','i','j','x','p','q','r','s','t','a','c','d','e','b','f','k','l','m','n','o','y','z']
length=len(password)
cnt=[0]*length

n=int(input())
words=[input().rstrip() for _ in range(n)]
max_idx=0

for word in words:
    cnt=[0]*length
    for w in word:
        if w!=' ':
            idx=password.index(w)
            cnt[idx]+=1
        else:
            continue
    max_idx=0
    max=cnt[0]
    same=0
    for i in range(len(cnt)):
        if max<cnt[i]:
            max_idx=i
            max=cnt[i]
    for i in range(len(cnt)):
        if max==cnt[i]:
            same+=1
    if same>1:
        print('?')
    else:
        print(password[max_idx])
    
       


