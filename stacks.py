class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def pop(self):
        if len(self.items) == 0:
            return None
        val = self.items[-1]
        del self.items[-1]
        return val

# s = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.pop()
# print(s.items)


def is_balanced(input_str):
    s = Stack()
    for c in input_str:
        if c == "(":
            s.push("ab")
        elif c == ")":
            popped = s.pop()
            if popped is None:
                return False
    val = s.peek()
    return val is None

print(is_balanced('()()(()))'))

