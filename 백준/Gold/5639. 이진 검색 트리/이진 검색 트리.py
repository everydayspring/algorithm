import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(start, end):
    if start > end:
        return
    root = preorder[start]
    idx = start + 1
    while idx <= end and preorder[idx] < root:
        idx += 1
    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)

postorder(0, len(preorder)-1)
