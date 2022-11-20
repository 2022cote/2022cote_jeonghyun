#GCD 합 https://www.acmicpc.net/problem/9613

#문제 접근
#1 list를 이용해서 gcd를 따로 모으고 sum(list)이용

#추가 메모
#1 문제를 이해 잘못해서 겹치는 gcd는 append하지 않아서 시간을 오래 뺏김..

import sys
input = sys.stdin.readline

from math import gcd

N = int(input())

for i in range(N):
    list_gcd = [] #list_gcd 초기화
    list = input().split()
    list.pop(0) #맨 앞 숫자의 개수는 삭제
    for j in list[:-1]: #[:-1] index slicing - index값 0부터 마지막 값의 -1까지
        list.remove(j)
        for k in list:
            list_gcd.append(gcd(int(j),int(k)))
    print(sum(list_gcd))