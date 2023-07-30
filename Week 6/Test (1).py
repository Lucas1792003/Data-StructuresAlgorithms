import sys
sys.setrecursionlimit(10001)
root = None

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class BinarySearchTree:
    def inorder_tree_walk(self, x):
        if x is not None:
            self.inorder_tree_walk(x.left)
            print(x.key)
            self.inorder_tree_walk(x.right)

    def tree_maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def tree_minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def transplant(self, u, v):
        if u.parent is None:
            root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def tree_insert(self, z):
        global root
        y = None
        x = root  
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            root = z 
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def tree_successor(self, x):
        if x.right is not None:
            return self.tree_minimum(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def tree_predecessor(self, x):
        if x.left is not None:
            return self.tree_maximum(x.left)
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    def tree_search(self, k):
        global root
        x = root  
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # Function to print the BSTree
    def print_call(self, node, indent, last):
        if node is not None:
            print(indent, end=' ')
            if last:
                print("R----", end=' ')
                indent += "     "
            else:
                print("L----", end=' ')
                indent += "|    "

            print(str(node.key))
            self.print_call(node.left, indent, False)
            self.print_call(node.right, indent, True)

    # Function to call print
    def print_bstree(self):
        self.print_call(root, "", True) 
class Test:
    def __init__(self):
        self.root = None
# Example test code below
bst = BinarySearchTree()

bst.tree_insert(Node(3, 'III'))
bst.tree_insert(Node(1, 'I'))
bst.tree_insert(Node(5, 'V'))

bst.print_bstree()

z = bst.tree_search(1)
print('------------------')
bst.tree_delete(z)
bst.print_bstree()
print('------------------')
bst.inorder_tree_walk(root)

