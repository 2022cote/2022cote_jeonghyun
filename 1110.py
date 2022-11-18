import sys
input = sys.stdin.readline

N = int(input())
a = N//10
b = N%10
i = 0

while True:
    c = a + b
    M = int(str(b) + str(c%10))
    a = M//10
    b = M%10
    i += 1
    print(M, i)
    if int(N) == int(M): # string형태에서는 ==로 같다 조건을 설정할 수 없는지?
        print(i)
        break


