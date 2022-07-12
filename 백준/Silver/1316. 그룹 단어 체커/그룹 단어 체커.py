#문자열 내 연속된 문자인지 판별하기 유형
n=int(input())
cnt=0
for _ in range(n):
    word=input()
    flag=0
    for i in range(len(word)):
        if word.find(word[i],i+1) -i>1:
            flag=1
            break
    if flag==0:
        cnt+=1
print(cnt)
