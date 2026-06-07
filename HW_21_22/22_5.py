from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

k = int(input())
start_vertices = list(map(int, input().split()))

distance = [-1] * (n + 1)
queue = deque()

for vertex in start_vertices:
    distance[vertex] = 0
    queue.append(vertex)

while queue:
    vertex = queue.popleft()

    for next_vertex in graph[vertex]:
        if distance[next_vertex] == -1:
            distance[next_vertex] = distance[vertex] + 1
            queue.append(next_vertex)

max_time = max(distance[1:])

for vertex in range(1, n + 1):
    if distance[vertex] == max_time:
        last_vertex = vertex
        break

print(max_time)
print(last_vertex)
