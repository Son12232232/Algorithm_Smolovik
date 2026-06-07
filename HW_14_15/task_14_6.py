import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def push_front(self, value):
        node = Node(value)
        node.next = self.first

        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.first.previous = node
            self.first = node

        self.length += 1

    def push_back(self, value):
        node = Node(value)
        node.previous = self.last

        if self.last is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self.length += 1

    def pop_front(self):
        if self.first is None:
            return None

        value = self.first.value
        self.first = self.first.next
        self.length -= 1

        if self.first is None:
            self.last = None
        else:
            self.first.previous = None

        return value

    def pop_back(self):
        if self.last is None:
            return None

        value = self.last.value
        self.last = self.last.previous
        self.length -= 1

        if self.last is None:
            self.first = None
        else:
            self.last.next = None

        return value

    def front(self):
        if self.first is None:
            return None

        return self.first.value

    def back(self):
        if self.last is None:
            return None

        return self.last.value

    def size(self):
        return self.length

    def clear(self):
        self.first = None
        self.last = None
        self.length = 0


deque = Deque()

for line in sys.stdin:
    command = line.split()

    if not command:
        continue

    if command[0] == "push_front":
        deque.push_front(int(command[1]))
        print("ok")

    elif command[0] == "push_back":
        deque.push_back(int(command[1]))
        print("ok")

    elif command[0] == "pop_front":
        value = deque.pop_front()
        print("error" if value is None else value)

    elif command[0] == "pop_back":
        value = deque.pop_back()
        print("error" if value is None else value)

    elif command[0] == "front":
        value = deque.front()
        print("error" if value is None else value)

    elif command[0] == "back":
        value = deque.back()
        print("error" if value is None else value)

    elif command[0] == "size":
        print(deque.size())

    elif command[0] == "clear":
        deque.clear()
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break
