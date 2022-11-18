import sys
input = sys.stdin.readline

N = int(input())
#2부터 2+k(k는 자연수)를 하면서 나누어지는지 확인
k = 2
while True:
    if N%k ==0:
        print(k)
        N = N/k
    else : 
        k += 1
    if N == 1:
        break
    
        
    