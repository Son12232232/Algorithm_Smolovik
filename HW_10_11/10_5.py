import sys

for line in sys.stdin:
    data = list(map(int, line.split()))

    if len(data) < 2:
        continue

    capacity = data[0]
    track_count = data[1]
    tracks = data[2:2 + track_count]

    best_sum = 0
    stack = [(0, 0)]

    while stack:
        index, current_sum = stack.pop()

        if current_sum > capacity:
            continue

        if current_sum > best_sum:
            best_sum = current_sum

        if best_sum == capacity:
            break

        if index < track_count:
            stack.append((index + 1, current_sum))
            stack.append(
                (index + 1, current_sum + tracks[index])
            )

    print("sum:" + str(best_sum))
