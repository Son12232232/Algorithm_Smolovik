n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if times[j] < times[min_index]:
            min_index = j

    times[i], times[min_index] = times[min_index], times[i]

for current_time in times:
    print(*current_time)
