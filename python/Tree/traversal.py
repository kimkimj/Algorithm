# https://deeppago.tistory.com/m/8

n = int(input())
arr = [input().split() for _ in range(n)]
tree = {}

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

# root, left, right
def preorder(node):
    print(node.name, end="")
  # if node.left:
    if node.left != '.':
      # preorder(node.left)
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

# left, root, right
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.name, end='')
    if node.right!= '.':
        inorder(tree[node.right])

# left, right, node
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.name, end='')

for name, left, right in arr:
    tree[name] = Node(name, left, right)
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])