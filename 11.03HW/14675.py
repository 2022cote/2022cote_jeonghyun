import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for i in range(q):
    t,k=map(int,input().split())
    if t == 1:
        if(len(tree[k])<2):
            print("no")
        else:
            print("yes")
    
    elif t == 2:
        print("yes") #모든 간선이 단절선
