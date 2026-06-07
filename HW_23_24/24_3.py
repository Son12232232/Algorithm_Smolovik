m, n = map(int, input().split())

field = [list(input().strip()) for _ in range(m)]

parts = 0

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

for start_row in range(m):
    for start_column in range(n):
        if field[start_row][start_column] == "#":
            parts += 1

            stack = [(start_row, start_column)]
            field[start_row][start_column] = "."

            while stack:
                row, column = stack.pop()

                for dr, dc in directions:
                    new_row = row + dr
                    new_column = column + dc

                    if 0 <= new_row < m and 0 <= new_column < n:
                        if field[new_row][new_column] == "#":
                            field[new_row][new_column] = "."
                            stack.append((new_row, new_column))

print(parts)
