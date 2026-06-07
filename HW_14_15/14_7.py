import sys


class Node:
    pass


class Queue:
    pass


def create_queue(values):
    queue = Queue()
    queue.first = None
    queue.last = None
    queue.length = 0

    for value in values:
        push(queue, value)

    return queue


def push(queue, value):
    node = Node()
    node.value = value
    node.next = None

    if queue.last is None:
        queue.first = node
        queue.last = node
    else:
        queue.last.next = node
        queue.last = node

    queue.length += 1


def pop(queue):
    value = queue.first.value
    queue.first = queue.first.next
    queue.length -= 1

    if queue.first is None:
        queue.last = None

    return value


data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
half = n // 2

first_queue = create_queue(data[1:1 + half])
second_queue = create_queue(data[1 + half:1 + n])

moves = 0
limit = 200000

while (
    first_queue.length > 0
    and second_queue.length > 0
    and moves < limit
):
    first_card = pop(first_queue)
    second_card = pop(second_queue)

    first_wins = (
        first_card > second_card
        and not (first_card == n - 1 and second_card == 0)
    ) or (
        first_card == 0 and second_card == n - 1
    )

    if first_wins:
        push(first_queue, first_card)
        push(first_queue, second_card)
    else:
        push(second_queue, first_card)
        push(second_queue, second_card)

    moves += 1


if first_queue.length == 0:
    print("second", moves)
elif second_queue.length == 0:
    print("first", moves)
else:
    print("draw")
