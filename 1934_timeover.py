import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a, b = map(int,input().split())
    #최소공배수는 더 큰 수부터, 두 수의 곱까지 나누어 떨어지는 값을 찾는다
    for i in range((max(a,b)),(a*b)+1): 
        if i%a==0 and i%b==0:
            print(i)
            break