#삼각수 배열을 미리 만들고 for문을 돌리기
T=[n*(n+1)//2 for n in range(1,46)]

N=int(input())

for _ in range(N):
   v=int(input())
   flag = 0
   for i in range(len(T)):
      for j in range(len(T)):
         for k in range(len(T)):
            if T[i] + T[j] + T[k] == v:
               flag=1
               break
         if flag==1:
            break
      if flag==1:
         break
   print(flag)





