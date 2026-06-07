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

    def Print(self) -> None:
        current = self.head

        while current is not None:
            print(
                current.data,
                end=" " if current.next is not None else ""
            )
            current = current.next

        print()

    def _print_reverse(self, node: Node | None) -> None:
        if node is None:
            return

        self._print_reverse(node.next)

        print(
            node.data,
            end=" " if node is not self.head else ""
        )

    def PrintReverse(self) -> None:
        self._print_reverse(self.head)
        print()


data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
linked_list = List()

for i in range(1, n + 1):
    linked_list.addToTail(data[i])

linked_list.Print()
linked_list.PrintReverse()
