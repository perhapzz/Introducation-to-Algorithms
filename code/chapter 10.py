# Data Struct
# Stack
class Stack:
    """栈"""

    def __init__(self):
        self.data = []
        self.size = 0

    def empty(self):
        return self.size == 0

    def push(self, n):
        self.data.append(n)
        self.size += 1

    def pop(self):
        if self.size < 1:
            return None
        else:
            self.size -= 1
            return self.data.pop()

# Queue
class Queue:
    """队列"""

    def __init__(self):
        self.data = []
        self.size = 0

    def empty(self):
        return self.size == 0

    def push(self, n):
        self.data.append(n)
        self.size += 1

    def pop(self):
        if self.empty():
            return None
        self.size -= 1
        return self.data.pop(0)

# Linked List
