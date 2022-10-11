import sys

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
for i in range(N):
    array = input()
    arr = array.split()
    SIZE = int(arr[0])

    queue =[ None for _ in range(SIZE) ]  # queue정의

    importance = input() #중요도 입력

    for j in range(len(importance)): #queue 채우기
        queue[j] = importance[j]

print(queue)