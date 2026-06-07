import sys


class StackNode:
    def __init__(self, value, previous=None):
        self.value = value
        self.previous = previous


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        self.top = StackNode(value, self.top)
        self.length += 1

    def pop(self):
        if self.top is None:
            return None

        value = self.top.value
        self.top = self.top.previous
        self.length -= 1
        return value

    def back(self):
        if self.top is None:
            return None
        return self.top.value

    def size(self):
        return self.length

    def clear(self):
        self.top = None
        self.length = 0


def main():
    stack = Stack()
    answers = []

    for line in sys.stdin:
        command = line.strip().split()

        if not command:
            continue

        if command[0] == "push":
            stack.push(int(command[1]))
            answers.append("ok")

        elif command[0] == "pop":
            value = stack.pop()
            answers.append("error" if value is None else str(value))

        elif command[0] == "back":
            value = stack.back()
            answers.append("error" if value is None else str(value))

        elif command[0] == "size":
            answers.append(str(stack.size()))

        elif command[0] == "clear":
            stack.clear()
            answers.append("ok")

        elif command[0] == "exit":
            answers.append("bye")
            break

    print("\n".join(answers))


if __name__ == "__main__":
    main()
