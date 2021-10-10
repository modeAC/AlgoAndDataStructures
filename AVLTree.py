class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.size = 0

    def insert(self, root, key, value):
        if root is None:
            self.size += 1
            return Node(key, value)
        elif key < root.key:
            root.left = self.insert(root.left, key, value)
        else:
            root.right = self.insert(root.right, key, value)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)
        if balance > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def get(self,root, key):
        if root is not None:
            if root.key == key:
                return root.value
            elif root.key > key:
                return self.get(root.left, key)
            else:
                return self.get(root.right, key)
        return None

    def sz(self):
        return self.size

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def Inorder(self, root, arr):
        if root:
            self.Inorder(root.left, arr)
            arr.append(root.key)
            self.Inorder(root.right, arr)
            return arr

class TreeSet:
    def __init__(self):
        self.tree = AVLTree()
        self.root = None

    def add(self, key):
        if key not in self:
            self.root = self.tree.insert(self.root, key, key)

    def __contains__(self, item):
        search = self.tree.get(self.root, item)
        return search is not None

    def __len__(self):
        return self.tree.size
