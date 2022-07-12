import sys
input=sys.stdin.readline
n=int(input())

per=[int(input()) for _ in range(n)]
#팁은 돈-인덱스이므로 인덱스 값이 커질수록 돈도 커져야 음수가 되는 경우를 막을 수 있다.
#그래서 돈의 순서를 내림차순 정렬해준다.
per.sort(reverse=True)
tip=0
for i in range(n):
    if per[i]-i<0:
        continue
    tip+=per[i]-i
print(tip)
