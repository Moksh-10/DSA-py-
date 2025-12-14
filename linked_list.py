# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class ll:
#     def __init__(self):
#         self.head = None
#
#     # O(n)
#     def __repr__(self):
#         if self.head is None:
#             return "[]"
#         else:
#             last = self.head
#             rstr = f"[{last.value}"
#             while last.next:
#                 last = last.next
#                 rstr += f", {last.value}"
#             rstr += "]"
#             return rstr
#
#     # O(n)
#     def __contains__(self, value):
#         last = self.head
#         while last is not None:
#             if last.value == value:
#                 return True
#             last = last.next
#         return False
#
#     # O(n)
#     def __len__(self): # can be implemented in constant time, you can keep size in Node class and increase / decrease at every step
#         last = self.head
#         c = 0
#         while last is not None:
#             c += 1
#             last = last.next
#         return c
#
#     # O(n)
#     def append(self, value):
#         if self.head is None:
#             self.head = Node(value)
#         else:
#             last = self.head
#             while last.next:
#                 last = last.next
#             last.next = Node(value)
#
#     # O(1)
#     def prepend(self, value):
#         first = Node(value)
#         first.next = self.head
#         self.head = first
#
#     # O(n)
#     def insert(self, value, index):
#         if index == 0:
#             self.prepend(value)
#         else:
#             if self.head is None:
#                 raise ValueError("index out of bounds")
#             else:
#                 last = self.head
#                 for i in range(index-1):
#                     if last.next is None:
#                         raise ValueError("index out of bounds")
#                     last = last.next
#                 new_node = Node(value)
#                 new_node.next = last.next
#                 last.next = new_node
#
#     # O(n)
#     def delete(self, value):
#         last = self.head
#         if last is not None:
#             if last.value == value:
#                 self.head = last.next
#             else:
#                 while last.next:
#                     if last.next.value == value:
#                         last.next = last.next.next
#                         break
#                     last = last.next
#
#     # O(n)
#     def pop(self, index):
#         if self.head is None:
#             raise ValueError("index out of bounds")
#         else:
#             last = self.head
#             for i in range(index - 1):
#                 if last.next is None:
#                     raise ValueError("index out of bounds")
#                 last = last.next
#             if last.next is None:
#                 raise ValueError("index out of bounds")
#             else:
#                 last.next = last.next.next
#
#     # O(n)
#     def get(self, index):
#         if self.head is None:
#             raise ValueError("index out of bounds")
#         else:
#             last = self.head
#             for i in range(index):
#                 if last.next is None:
#                     raise ValueError("index out of bounds")
#                 last = last.next
#             return last.value
#
# if __name__ == "__main__":
#     ll = ll()
#
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     ll.append(40)
#     ll.prepend(100)
#     ll.insert(300, 1)
#     ll.delete(30)
#     ll.pop(1)
#     print(ll.get(1))
#     print(33 in ll)
#     print(ll)
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class dll:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(n)
    def __repr__(self):
        if self.head is None:
            return "[]"
        else:
            last = self.head
            rstr = f"[{last.value}"
            while last.next:
                last = last.next
                rstr += f", {last.value}"
            rstr += "]"
            return rstr

    # O(n)
    def __contains__(self, value):
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n)
    def __len__(self): # can be implemented in constant time, you can keep size in Node class and increase / decrease at every step
        last = self.head
        c = 0
        while last is not None:
            c += 1
            last = last.next
        return c

    # O(n)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            last = Node(value)
            last.previous = self.tail
            self.tail.next = last
            self.tail = last

    # O(1)
    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            first = Node(value)
            first.next = self.head
            self.head.previous = first
            self.head = first

    # O(n)
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("index out of bounds")
            else:
                last = self.head
                for i in range(index-1):
                    if last.next is None:
                        raise ValueError("index out of bounds")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                new_node.previous = last
                if last.next is not None:
                    last.next.previous = new_node
                last.next = new_node

    # O(n)
    def delete(self, value):
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        if last.next.next is not None:
                            last.next.next.previous = last
                        last.next = last.next.next
                        break
                    last = last.next

    # O(n)
    def pop(self, index):
        if self.head is None:
            raise ValueError("index out of bounds")
        else:
            last = self.head
            for i in range(index - 1):
                if last.next is None:
                    raise ValueError("index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("index out of bounds")
            else:
                if last.next.next is not None:
                    last.next.next.previous = last
                last.next = last.next.next

    # O(n)
    def get(self, index):
        if self.head is None:
            raise ValueError("index out of bounds")
        else:
            last = self.head
            for i in range(index):
                if last.next is None:
                    raise ValueError("index out of bounds")
                last = last.next
            return last.value

if __name__ == "__main__":
    ll = dll()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.prepend(100)
    ll.insert(300, 1)
    ll.delete(30)
    ll.pop(1)
    print(ll.get(1))
    print(33 in ll)
    print(ll)


