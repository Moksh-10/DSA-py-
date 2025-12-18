class min_heap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def __repr__(self):
        return str(self.heap)

    def insert(self, key, value):
        self.heap.append((key, value))
        self._sift_up(len(self.heap) - 1)

    def peek_min(self):
        if not self.heap:
            raise IndexError("empty heap")
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            raise IndexError("empty heap")
        min_ele = self.heap[0]
        last_ele = self.heap.pop()

        if self.heap:
            self.heap[0] = last_ele
            self._sift_down(0)

        return min_ele

    def heapify(self, elements):
        self.heap = list(elements)



    def meld(self, other_heap):
        pass

    def _parent(self, index):
        return (index + 1) // 2 if index != 0 else None

    def _left(self, index):
        lef = 2 * index + 1
        return lef if lef < len(self.heap) else None

    def _right(self, index):
        rig = 2 * index + 2
        return rig if rig < len(self.heap) else None

    def _sift_up(self, index): #swim
        pi = self._parent(index)

        while pi is not None and self.heap[index][0] < self.heap[pi][0]:
            self.heap[index], self.heap[pi] = self.heap[pi], self.heap[index]
            index = pi
            pi = self._parent(index)

    def _sift_down(self, index): #sink
        while True:
            sm = index
            left = self._left(index)
            right = self._right(index)

            if left is not None and self.heap[left][0] < self.heap[sm][0]:
                sm = left

            if right is not None and self.heap[right][0] < self.heap[sm][0]:
                sm = right

            if sm == index:
                break
            self.heap[index], self.heap[sm] = self.heap[sm], self.heap[index]
            index = sm


