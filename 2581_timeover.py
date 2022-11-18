import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
list = []
for i in range(M,N+1):
    j = 0
    num = 0
    for j in range(i+1):
        if i%(j+1) == 0:
            num += 1
    print(num)
    if num == 2:
        list.append(i)
print(list)
print(sum(list))
print(min(list))