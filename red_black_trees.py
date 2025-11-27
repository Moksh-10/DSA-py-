class rbnode:
    def __init__(self):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class rbtree:
    def __init__(self):
        self.nil = rbnode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = rbnode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return



