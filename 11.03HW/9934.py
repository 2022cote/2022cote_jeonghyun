import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))
tree = [[] for _ in range(N)]

def Tree(input_list, x):
    root = (len(input_list)//2) #root node는 항상 2로 나눈 몫
    tree[x].append(input_list[root])

    if len(input_list) == 1:
        return
    Tree(input_list[:root],x+1)
    Tree(input_list[root+1:],x+1)

Tree(num_list,0)
for i in range(N):
    print(*tree[i])