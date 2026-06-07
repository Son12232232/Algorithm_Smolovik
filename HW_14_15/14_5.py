import sys


class Node:
    pass


class Queue:
    pass


def push(queue, value):
    new_node = Node()
    new_node.value = value
    new_node.next = None

    if queue.last is None:
        queue.first = new_node
        queue.last = new_node
    else:
        queue.last.next = new_node
        queue.last = new_node

    queue.length += 1


def pop(queue):
    if queue.first is None:
        return None

    value = queue.first.value
    queue.first = queue.first.next
    queue.length -= 1

    if queue.first is None:
        queue.last = None

    return value


def front(queue):
    if queue.first is None:
        return None

    return queue.first.value


def clear(queue):
    queue.first = None
    queue.last = None
    queue.length = 0


queue = Queue()
queue.first = None
queue.last = None
queue.length = 0

for line in sys.stdin:
    command = line.strip().split()

    if not command:
        continue

    if command[0] == "push":
        push(queue, int(command[1]))
        print("ok")

    elif command[0] == "pop":
        value = pop(queue)

        if value is None:
            print("error")
        else:
            print(value)

    elif command[0] == "front":
        value = front(queue)

        if value is None:
            print("error")
        else:
            print(value)

    elif command[0] == "size":
        print(queue.length)

    elif command[0] == "clear":
        clear(queue)
        print("ok")

    elif command[0] == "exit":
        print("bye")
        break
