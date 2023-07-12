import sys

input = sys.stdin.readline

n = int(input())
tree = {}

# dictionary[root] = [left, right]
# 자식 노드가 없는 경우에는 .
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(root):
    # if the node is not the leaf node
    if root != '.':
        print(root, end = '') # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

def inorder(root):
    if root != '.':
        inorder(tree[root][0]) # left
        print(root, end = '')
        inorder(tree[root][1]) # right

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')


preorder('A')
print()
inorder('A')
print()
postorder('A')
