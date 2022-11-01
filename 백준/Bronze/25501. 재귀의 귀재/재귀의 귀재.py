import sys
input=sys.stdin.readline

cnt=0

def recursion(s,l,r):
    global cnt
    cnt+=1
    if l>=r: return 1
    elif s[l] !=s[r]: return 0
    else: return recursion(s,l+1,r-1)

def isPalindrome(s):
    return recursion(s,0,len(s)-1)

n=int(input())
word=[]
for i in range(n):
    cnt=0
    word.append(input().rstrip())
    print(isPalindrome(word[i]),cnt)