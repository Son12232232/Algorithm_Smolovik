import sys
from collections import deque

input = sys.stdin.buffer.readline

n = int(input())
field = [list(input().decode().strip()) for _ in range(n)]

start = None
finish = None

for i in range(n):
    for j in range(n):
        if field[i][j] == "@":
            start = (i, j)
        elif field[i][j] == "X":
            finish = (i, j)

parent = [[None] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

queue = deque([start])
visited[start[0]][start[1]] = True

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

while queue:
    row, column = queue.popleft()

    if (row, column) == finish:
        break

    for dr, dc in directions:
        new_row = row + dr
        new_column = column + dc

        if 0 <= new_row < n and 0 <= new_column < n:
            if not visited[new_row][new_column]:
                if field[new_row][new_column] in ".X":
                    visited[new_row][new_column] = True
                    parent[new_row][new_column] = (row, column)
                    queue.append((new_row, new_column))

if not visited[finish[0]][finish[1]]:
    print("N")
else:
    current = finish

    while current != start:
        row, column = current
        field[row][column] = "+"
        current = parent[row][column]

    print("Y")

    for row in field:
        print("".join(row))
