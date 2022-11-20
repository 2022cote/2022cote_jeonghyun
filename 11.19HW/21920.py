#서로소 평균 https://www.acmicpc.net/problem/21920
#문제 접근
#1. 서로소는 같은 소수가 1을 제외하고는 없음 > 일단 소수를 각각 구한다
#2. gcd가 1이면 서로소이다.
#추가 메모

import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
a = input().split()
a = list(map(int,a))
num = int(input())
sum = 0
k = 0
for i in a:
    if gcd(i,num) == 1:
        sum += i
        k += 1

print(sum/k)
