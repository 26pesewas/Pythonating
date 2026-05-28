from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    # add items rightward of the deque
    def push(self, value):
        self.container.append(value)

    def pop(self):
        #returns last item in the deque and removes it from the deque
        return self.container.pop()

    def peek(self):
        #returns last item in the deque
        return self.container[-1]

    def is_empty(self):
        # return true if deque is empty and false if it is not
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def insert_value(self, index, value):
        # insert value into the deque at position index
        return self.container.insert(index, value)


def reverse_string(s):
    d = Stack()
    for char in s:
        d.push(char)

    rev_d = ''
    while d.size() != 0:
        rev_d += d.pop()

    return rev_d



print(reverse_string("We will conquer COVID-19"))
