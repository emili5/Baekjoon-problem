ch=input()
for i in range(ord('a'),ord('z')+1):
    for j in range(len(ch)):
        a=-1 #초기화 위치
        if chr(i) == ch[j]:
            a=j
            break #인덱스 찾았으면 빠져나가기
    print(a,end=" ")