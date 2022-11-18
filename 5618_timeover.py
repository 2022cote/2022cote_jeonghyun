import time
s = time.time()
import sys
input = sys.stdin.readline

N = int(input())
list2 = []
list3 = []
if N == 2:
    a, b = map(int,input().split())
    for i in range(a):
        if a%(i+1) == 0:
            list2.append(i+1)
    for i in list2:
        if b%int(i) == 0:
            print(i)
else :
    a, b, c = map(int,input().split())
    for i in range(a):
        if a%(i+1) == 0:
            list2.append(i+1)
    for i in list2:
        if b%int(i) == 0:
            list3.append(i)
    for i in list3:
        if c%int(i) == 0:
            print(i)

print('소요시간 : ', time.time()-s)