import sys
sys.setrecursionlimit(10**6)
n = int(input())
tree = {}
for _ in range(n):
    p, l, r = input().split()
    tree[p] = (l, r)
def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])
def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')
