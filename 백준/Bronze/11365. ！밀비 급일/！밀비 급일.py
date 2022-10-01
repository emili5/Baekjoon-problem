import sys

input=sys.stdin.readline

def inp():
    return input().rstrip()

while True:
    result=inp()
    if result=="END":
        break
    print(result[::-1])
