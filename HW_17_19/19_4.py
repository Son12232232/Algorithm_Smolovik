import sys


class PriorityQueue:
    def __init__(self):
        # Елементи купи мають вигляд [priority, id]
        self.heap = []

        # position[id] — індекс елемента в купі
        self.position = {}

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        self.position[self.heap[i][1]] = i
        self.position[self.heap[j][1]] = j

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent][0] >= self.heap[i][0]:
                break

            self.swap(parent, i)
            i = parent

    def sift_down(self, i):
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == i:
                break

            self.swap(i, largest)
            i = largest

    def add(self, element_id, priority):
        self.heap.append([priority, element_id])

        index = len(self.heap) - 1
        self.position[element_id] = index

        self.sift_up(index)

    def pop(self):
        priority, element_id = self.heap[0]

        last = self.heap.pop()
        del self.position[element_id]

        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self.sift_down(0)

        return element_id, priority

    def change(self, element_id, new_priority):
        index = self.position[element_id]
        old_priority = self.heap[index][0]

        self.heap[index][0] = new_priority

        if new_priority > old_priority:
            self.sift_up(index)
        else:
            self.sift_down(index)


queue = PriorityQueue()
answer = []

for line in sys.stdin:
    command = line.split()

    if not command:
        continue

    if command[0] == "ADD":
        element_id = command[1]
        priority = int(command[2])

        queue.add(element_id, priority)

    elif command[0] == "POP":
        element_id, priority = queue.pop()
        answer.append(f"{element_id} {priority}")

    elif command[0] == "CHANGE":
        element_id = command[1]
        new_priority = int(command[2])

        queue.change(element_id, new_priority)

print("\n".join(answer))
