import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int,input().split()))
num = 0 #소수의 개수
for i in numbers:
    k = 0 #약수의 개수

    for j in range(i):
        if int(i)%int(j+1) == 0:
            k += 1
        if k == 2:
            num += 1
print(num)
        
        