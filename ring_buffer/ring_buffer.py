from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        else:
            self.current.value = item
            self.current = self.current.prev

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cur = self.storage.tail
        while cur is not self.storage.head:
            list_buffer_contents.append(cur.value)
            cur = cur.prev
        list_buffer_contents.append(self.storage.head.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None for i in range(0, self.capacity)]

    def append(self, item):
        self.storage[self.current] = item
        self.current += 1
        if self.current + 1 > self.capacity:
            self.current = 0

    def get(self):
        returned_arr = []
        for el in self.storage:
            if el is not None:
                returned_arr.append(el)
        return returned_arr