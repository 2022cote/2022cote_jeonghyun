import sys
input = sys.stdin.readline
tree={}

N=int(input())

for n in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

def pre(root):
    if root != '.':
        print(root, end='')
        pre(tree[root][0])
        pre(tree[root][1])

def inorder(root):
    if root != '.':  #root =='.'이면 다음 줄 진행
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

pre('A')
print()#pre와 inorder 사이의 줄바꿈
inorder('A')
print()#inorder과 postorder 사이의 줄바꿈
postorder('A')
        