import time
s = time.time()
import sys
input = sys.stdin.readline

N = int(input())
Nlist = list(map(int,input().split()))
gcd=[]

for i in range(1, int(((min(Nlist)+1)/2)+1)):
    if N ==2:
        if Nlist[0]%i == 0 and Nlist[1]%i == 0:
            print(i)
    else:
        if Nlist[0]%i == 0 and Nlist[1]%i == 0 and Nlist[2]%i ==0:
            print(i)

print('소요시간 : ', time.time()-s)