#소수 최소 공배수 https://www.acmicpc.net/problem/21919

#문제 접근

#추가 메모
#1. lcm에 list형태로는 대입 불가능 따로 함수를 정의해야한다.
#2. 근데 소수끼리는 최소공배수가 그냥 자기들끼리 곱한 값이다.

import sys
input = sys.stdin.readline
from math import gcd,lcm,sqrt

def isPrime(a):
    a = int(a)
    k = 0
    for i in range(1,int(sqrt(a))+1):
        if a%(i) == 0:
            k+=1
    if k == 1:
        return 1
    else:
        return 0

N = int(input())
numbers = input().split()
primenums = []
for i in numbers:
    if isPrime(i) == 1:
        if i not in primenums:
            primenums.append(i)

p = 1
for i in primenums:
    p = p*int(i)

if len(primenums) == 0:
    print('-1')
else:
    print(p)
