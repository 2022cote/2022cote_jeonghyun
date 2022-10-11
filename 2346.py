import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

list=[]
N = int(input())
deq = deque(enumerate(map(int,input().split()))) # tuple로 

for i in range(N):
    p = deq.popleft() # LIFO,  p = (0,deq) , deque >> stack

    list.append(p[0]+1) #풍선 번호 list에 입력
    if p[1] > 0:
        deq.rotate(-((p[1])-1))
    else:
        deq.rotate(-p[1])

print(' '.join(map(str, list))) #list int값 str바꿔서 ' '와 함께 출력
  