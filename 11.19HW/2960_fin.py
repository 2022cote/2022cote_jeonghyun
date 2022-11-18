#에라토스테네스의 체 https://www.acmicpc.net/problem/2960

#문제 접근
#1 list를 두 개 두고 삭제와 입력을 반복 > break이 실행이 안됨
#2 위의 방법보단 False로 이루어진 list의 value를 True로 바꿔가면서 풀이.
#추가 메모
#python의 list에서의 remove와 pop의 차이

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tmp = 0
list = [True] * (N + 1)
for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if list[j] != False:
            list[j] = False
            tmp += 1
            if tmp == K:
                print(j)
