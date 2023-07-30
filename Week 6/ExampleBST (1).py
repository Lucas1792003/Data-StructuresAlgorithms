from Test import *

x = []
for k in [56, 26, 200, 18, 28, 190, 213, 12, 24, 27]:
    x.append(Node(k, None))

T = Test()

T.root = x[0]
for i in range(len(x) // 2):
    if 2 * i + 1 < len(x):
        x[i].left = x[2 * i + 1]
        x[2 * i + 1].parent = x[i]
    if 2 * (i + 1) < len(x):
        x[i].right = x[2 * (i + 1)]
        x[2 * (i + 1)].parent = x[i]

bst = BinarySearchTree()
bst.root = T.root


bst.inorder_tree_walk(bst.root)