class bstnode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val:
            if self.left is None:
                self.left = bstnode(val)
                return
            self.left.insert(val)
            return
        if self.right is None:
            self.right = bstnode(val)
            return
        self.right.insert(val)
        return

    def get_min(self):
        temp = self
        while temp.left is not None:
            temp = temp.left
        return temp.val

    def get_max(self):
        temp = self
        while temp.right is not None:
            temp = temp.right
        return temp.val

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        if not self.right:
            return self.left
        if not self.left:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node
        self.right = self.right.delete(min_larger_node.val)
        return self

    def preorder(self, visited):
        visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited

    def postorder(self, visited):
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited

    def inorder(self, visited):
        if self.left:
            visited = self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            visited = self.right.inorder(visited)
        return visited

    def exists(self, val):
        if self.val == val:
            return True
        if val < self.val and self.left:
            return self.left.exists(val)
        if val > self.val and self.right:
            return self.right.exists(val)
        return False


