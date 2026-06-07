from __future__ import annotations
import sys


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node | None = None


class List:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None

    def addToTail(self, val: int) -> None:
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def ReorderList(self) -> None:
        if self.head is None or self.head.next is None:
            return

        slow = self.head
        fast = self.head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        previous = None

        while second is not None:
            next_node = second.next
            second.next = previous
            previous = second
            second = next_node

        first = self.head
        second = previous

        while second is not None:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        self.tail = self.head

        while self.tail.next is not None:
            self.tail = self.tail.next

    def Print(self) -> None:
        current = self.head

        while current is not None:
            print(
                current.data,
                end=" " if current.next is not None else ""
            )
            current = current.next

        print()


data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
linked_list = List()

for i in range(1, n + 1):
    linked_list.addToTail(data[i])

linked_list.ReorderList()
linked_list.Print()
