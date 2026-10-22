"""Singly linked list."""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_tail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def delete(self, value):
        cur, prev = self.head, None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False

    def search(self, value):
        return value in self.to_list()

    def to_list(self):
        items, cur = [], self.head
        while cur:
            items.append(cur.value)
            cur = cur.next
        return items
