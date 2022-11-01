import sys
input = sys.stdin.readline
tree={}

N = int(input())
list = input().split()

for i in range(N): #tree를 dictionary를 통해 구현
    tree[i]=int(list[i])

del_node = int(input()) 

def delete(x): #del_node가 포함된 노드는 tree에서 삭제 (ㅜㅜ)
    for i in range(len(tree)):
        if x == tree[i]:
            delete(i)
            del(tree[i])
        del(tree[i])

def count(tree): #tree에서 자식 노드가 없는 노드의 개수 찾기
    j = 0
    for i in tree.keys():
        if i not in tree.values():
            j += 1
    print(j)

delete(del_node)
count(tree)