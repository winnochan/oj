#!/usr/bin/env python


class DllNode:
    def __init__(self, key: int, val: int, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt
        return


class LRUCache:
    def __init__(self, capacity: int):
        self.table = {}
        self.head = None
        self.tail = None
        self.capa = capacity
        return

    def get(self, key: int) -> int:
        if key in self.table:
            # if in table, update dll position
            node = self.table[key]

            # if node is head
            if node == self.head:
                return node.val

            # if node is tail
            if node == self.tail:
                self.tail = node.pre
                self.tail.nxt = None

                node.pre = None
                node.nxt = self.head
                self.head.pre = node
                self.head = node
                return node.val

            # if node is both not head and tail
            node.pre.nxt = node.nxt
            node.nxt.pre = node.pre
            node.pre = None
            node.nxt = self.head
            self.head = node

            return node.val

        return -1

    def put(self, key: int, val: int) -> None:
        if self.capa <= 0:
            return

        if key in self.table:
            self.get(key)
            node = self.table[key]
            node.val = val
        else:
            node = DllNode(key, val)
            self.table[key] = node
            if len(self.table) == 1:
                self.head = self.tail = node
                return
            node.nxt = self.head
            self.head.pre = node
            self.head = node
            if len(self.table) > self.capa:
                self.table.pop(self.tail.key)
                self.tail = self.tail.pre
                self.tail.nxt = None
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,val)
