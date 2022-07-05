ch=input()
for i in range(ord('a'),ord('z')+1):
    if chr(i) in ch:
        #문자열 내 찾고 싶은 문자를 매개변수로 보내면 인덱스값 반환
        print(ch.find(chr(i)),end=" ")
    else:
        print(-1, end=" ")