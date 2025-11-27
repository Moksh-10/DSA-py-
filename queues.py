class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        val = self.items[-1]
        del self.items[-1]

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.items)
q.pop()
print(q.peek())
print(q.items)

