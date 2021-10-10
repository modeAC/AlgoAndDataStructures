class Node:
    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0


    def push(self, value):
        self.value = value
        new_node = Node(value, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node


    def pop(self):
        if self.tail != self.head:
            curr = self.tail.prev
            self.tail = None
            self.tail = curr
            self.tail.next = None
        else:
            self.tail = None
            self.head = None
        return self.tail


    def unshift(self, value):
        new_node = Node(value, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head = new_node


    def shift(self):
        if self.tail != self.head:
            curr = self.head.next
            self.head = None
            self.head = curr
            self.head.prev = None
        else:
            self.tail = None
            self.head = None
        return self.head


    def insert(self, index, value):
        self.index = index
        self.value = value
        new_node = Node(value, None, None)
        if index == 0 and self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        elif self.get(index) is not None:
            new_node.prev = self.get(index).prev
            new_node.next = self.get(index)
            self.get(index).prev  = new_node
            self.get(index - 1).next = new_node
        else:
            self.push(value)


    def find(self, value):
        self.value = value
        current_node = self.head
        while True:
            if current_node(value) == value:
                return value
            current_node = current_node.next


    def get(self, index):
        current_node = self.head
        count = 0
        while current_node is not None:
            if count == index:
                return current_node
            count += 1
            current_node = current_node.next
        return None

    def size(self):
        current_node = self.head
        count = 0
        while True:
            if current_node is None:
                return (count + 1)
                break
            count += 1
            current_node = current_node.next


    def print(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.prev
        print()
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next

