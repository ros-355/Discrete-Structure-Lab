"""
LAB 09: Tree Structures and Traversals

Required libraries:
- Python standard library only

Theory:
A tree is a hierarchical data structure.

Common binary-tree traversals:
Preorder : Root -> Left -> Right
Inorder  : Left -> Root -> Right
Postorder: Left -> Right -> Root

Aim:
1. Create a binary tree.
2. Perform preorder, inorder, and postorder traversals.

Conclusion:
Tree traversals visit the same nodes in different orders depending on the
required processing sequence.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


# Build this tree:
#         A
#       /   \
#      B     C
#     / \   / \
#    D   E F   G

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Preorder:")
preorder(root)

print("\n\nInorder:")
inorder(root)

print("\n\nPostorder:")
postorder(root)
print()
