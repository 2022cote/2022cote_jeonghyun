#다음 소수 https://www.acmicpc.net/problem/4134

#문제 접근

#추가 메모

import sys
input = sys.stdin.readline

def IsPrime(a):
    k = 0
    for i in range(1,int(a**0.5)+1):
        if a%(i) == 0:
            k += 1
    if k == 1:
        return 1
    else:
        return 0


N = int(input())
for i in range(N):
    num = int(input())
    while True:
        if IsPrime(num) == 1:
            print(num)
            break
        else: 
            num += 1


        
    
    
    
    



