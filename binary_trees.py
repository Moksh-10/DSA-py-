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

    # O(n) - worst  O(log n) - avg  O(h) - always
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

    # O(n)
    def __iter__(self):
        yield from self._in_order(self.root)

    # O(n)
    def __repr__(self):
        return str(list(self._in_order(self.root)))

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key)
            self.root.value = value
        else:
            cn = self.root
            while True:
                if key < cn.key:
                    if cn.left is None:
                        cn.left = Node(key)
                        cn.left.value = value
                        cn.left.parent = cn
                        break
                    else:
                        cn = cn.left
                elif key > cn.key:
                    if cn.right is None:
                        cn.right = Node(key)
                        cn.right.value = value
                        cn.right.parent = cn
                        break
                    else:
                        cn = cn.right
                else:
                    cn.value = value
                    break

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
        node = self.search(key)
        if node is None:
            raise KeyError('does not exist')
        self._delete(node)

    # O(n)
    def traverse(self, order):
        if order == 'inorder':
            yield from self._in_order(self.root)
        elif order == 'preorder':
            yield from self._pre_order(self.root)
        elif order == 'postorder':
            yield from self._post_order(self.root)
        else:
            raise ValueError("unknown order")

    def _delete(self, node: Node):
        # leaf node
        if node.left is None and node.right is None:
            if node.parent is None:
                self.root = None
            else:
                if node.parent.right == node:
                    node.parent.right = None
                else:
                    node.parent.left = None
                node.parent = None

        # has 1 child node
        elif node.left is None or node.right is None:
            chn = node.left if node.left is not None else node.right
            if node.parent is None:
                chn.parent = None
                self.root = chn
            else:
                if node.parent.right == node:
                    node.parent.right = chn
                else:
                    node.parent.left = chn
                chn.parent = node.parent
            node.parent = node.left = node.right = None

        # has 2 child node
        else:
            suc = self._successor(node)
            node.key = suc.key
            node.value = suc.value
            self._delete(suc)

    def _successor(self, node: Node):
        if node is None:
            raise ValueError('cannot find successor')
        if node.right is None:
            return None
        else:
            cn = node.right
            while cn.left is not None:
                cn = cn.left
            return cn

    def _predecessor(self, node: Node):
        if node is None:
            raise ValueError('cannot find predecessor')
        if node.left is None:
            return None
        else:
            cn = node.left
            while cn.right is not None:
                cn = cn.right
            return cn

    def _in_order(self, node: Node):
        if node is not None:
            yield from self._in_order(node.left)
            yield (node.key, node.value)
            yield from self._in_order(node.right)

    def _pre_order(self, node: Node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order(node.left)
            yield from self._pre_order(node.right)

    def _post_order(self, node: Node):
        if node is not None:
            yield from self._post_order(node.left)
            yield from self._post_order(node.right)
            yield (node.key, node.value)


if __name__ == "__main__":
    tr = bst()
    tr.insert(10, 'x')
    tr.insert(5, 'x')
    tr.insert(22, 'x')
    tr.insert(2, 'x')
    tr.insert(9, 'x')
    tr.insert(12, 'x')
    tr.insert(30, 'x')
    tr.insert(11, 'x')
    tr.insert(15, 'x')
    tr.insert(30, 'x')
    tr.insert(23, 'x')
    tr.insert(35, 'x')
    tr.delete(9)
    tr.delete(10)
    tr.insert(1, 'x')
    tr.delete(2)
    for i in tr.traverse('inorder'):
        print(i)
    print(tr)
    print(tr.search(30))

