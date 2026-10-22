"""Stack (last in, first out), built on a linked list of nodes."""
from .linked_list import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """Remove and return the top value, or None if the stack is empty."""
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        return None if self.top is None else self.top.value

    def is_empty(self):
        return self.top is None

    def to_list(self):
        """Items from top to bottom."""
        items, cur = [], self.top
        while cur:
            items.append(cur.value)
            cur = cur.next
        return items
