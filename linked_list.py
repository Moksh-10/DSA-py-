class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node


# l = Node("a")
# l.set_next(Node("b"))
# print(l.val, l.next)

class ll:
    def __init__(self):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
        last_node = None
        for n in self:
            last_node = n
        last_node.set_next(node)

    def add_to_head(self, node):
        node.next = self.head
        self.head = node
