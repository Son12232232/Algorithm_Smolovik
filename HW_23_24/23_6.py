from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    in_degree[v] += 1

queue = deque()

for vertex in range(1, n + 1):
    if in_degree[vertex] == 0:
        queue.append(vertex)

order = []

while queue:
    vertex = queue.popleft()
    order.append(vertex)

    for next_vertex in graph[vertex]:
        in_degree[next_vertex] -= 1

        if in_degree[next_vertex] == 0:
            queue.append(next_vertex)

if len(order) == n:
    print(*order)
else:
    print(-1)
