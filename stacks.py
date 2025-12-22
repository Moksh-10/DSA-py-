from re import S


class node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self) -> str:
        items = []
        cn = self.top
        while cn is not None:
            items.append(str(cn.value))
            cn = cn.next
        return ', '.join(items)
    
    def push(self, value):
        nn = node(value)
        nn.next = self.top
        self.top = nn
        self.size += 1

    def pop(self):
        if self.top is None:
            raise ValueError('stack is empty')
        pov = self.top.value
        self.top = self.top.next
        self.size -= 1
        return pov

    def peek(self):
        if self.top is None:
            raise ValueError('stack is empty')
        return self.top.value

    def is_empty(self):
        return self.top is None

if __name__ == "__main__":
    st = Stack()
    st.push(5)
    st.push(10)
    st.push(15)
    st.push(20)
    print(st)
    print(st.peek())
    print(st)
    print(st.pop())
    print(st)
    print(st.is_empty())

