class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"({self.key}, {self.value})"


class bst:
    def __init__(self):
        self.root = None

    def __contains__(self, key):
        cn = self.root
        while cn is not None:
            if key < cn.key:
                cn = cn.left
            elif key > cn.key:
                cn = cn.right
            else:
                return True
        return False

    def __iter__(self):
        pass

    def __repr__(self):
        pass

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value

    def search(self, key):
        cn = self.root
        while True:
            if cn is None or cn.key == key:
                return cn
            elif key < cn.key:
                if cn.left is None:
                   return None
                else:
                    cn = cn.left
            else:
                if cn.right is None:
                    return None
                else:
                    cn = cn.right

    def delete(self, key):
        pass

    def traverse(self, order):
        pass

    def _delete(self, key):
        pass

    def _successor(self, node):
        pass

    def _predecessor(self, node):
        pass

    def _in_order(self):
        pass

    def _pre_order(self):
        pass

    def _post_order(self):
        pass


