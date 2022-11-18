import time
s = time.time()
import sys
input = sys.stdin.readline

N = int(input())
Nlist = list(map(int,input().split()))

if N ==2:
    if Nlist[0]>Nlist[1]:
        r = Nlist%Nlist
            

print('소요시간 : ', time.time()-s)