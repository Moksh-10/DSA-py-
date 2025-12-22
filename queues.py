class node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def __repr__(self) -> str:
        items = []
        cn = self.front 
        while cn is not None:
            items.append(str(cn.value))
            cn = cn.next
        return ', '.join(items)

    def enqueue(self, value):
        nn = node(value)
        if self.rear is None:
            self.front = self.rear = nn
        else:
            self.rear.next = nn
            self.rear = nn
        self.size += 1

    def dequeue(self):
        if self.front is None:
            raise IndexError('queue is empty')
        dev = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1

    def peek(self):
        if self.front is None:
            raise IndexError('queue is empty')
        return self.front.value

    def is_empty(self):
        return self.front is None

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    q.dequeue()
    print(q)
    print(q.peek())
    print(q.is_empty())

