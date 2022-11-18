#소수&팰린드롬 https://www.acmicpc.net/problem/1747

#문제 접근
#1. 소수이면서 팰린드롬임을 만족하는 N값 출력

#추가 메모
#1. 팰린드롬? == 순서가 뒤집힌 숫자 ex)191..?
#2. 문자열 순서 뒤바꾸기 


import sys
import math
input = sys.stdin.readline

#소수 판별 함수 정의
def isPrime(a):
    k = 0
    for i in range(int(math.sqrt(a))+1):
        if a%(i+1) == 0:
            k+=1
    if k == 1:
        return True
    else:
        return False

#팰린드롬 판별 함수 정의
def isPalindrome(a):
    b = str(a)
    b = b[::-1]
    reversed_a = int(b)
    if a == reversed_a:
        return True
    else:
        return False

#두 조건 모두 만족시키는 N값 찾기
N = int(input())

for N in range(N,int(math.sqrt(100001))):
    if isPrime(N) and isPalindrome(N):
        print(N)
        break