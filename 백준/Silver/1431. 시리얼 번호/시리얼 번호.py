import sys
input= sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(input().rstrip())

#문자열 안에 포함된 숫자 전부를 더해 반환하는 함수
def sum_digit(a):
    tot=0
    for c in a:
        # 문자열 안에서 해당 문자가 숫자인지 판단해주는 메서드: isdigit()
        if c.isdigit():
            tot+=int(c)
    return tot

arr.sort(key=lambda x:(len(x),sum_digit(x),x))

for i in arr:
    print(i)