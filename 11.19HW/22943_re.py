#수 https://www.acmicpc.net/problem/22943

#문제 접근
#1. 서로 다른 소수의 합임을 확인
#   (소수)*(소수)*M^n(n은 양의 정수)인 수
# 위 두  조건을 모두 만족하는 수.
#추가 메모

import sys, math
input = sys.stdin.readline
condition1 = []
condition2 = []

#소수 판별 함수 정의
def isPrime(a):
    k = 0
    for i in range(1,int(math.sqrt(a))+1):
        if a%(i) == 0:
            k+=1
    if k == 1:
        return True
    else:
        return False

K, M = map(int,input().split())
#조건 1을 만족하는 값
for i in range(10**(K-1),10**K):
    if i == 1:
        continue
    else :
        for j in range(2,i):
            if isPrime(j) and isPrime(i-j):
                condition1.append(i)
print(condition1)

#조건 2를 만족하는 값
for i in condition1:
    origin_i = i
    while i%M == 0:
        i = i//M
    k = 0
    for j in range(2,int(math.sqrt(i))):
        if i%j == 0:
            k += 1
    if k == 1:
        condition2.append(origin_i)
print(condition2)
print(len(condition2))
