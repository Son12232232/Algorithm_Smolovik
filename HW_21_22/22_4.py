n, k, a, b, d = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(k):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False] * (n + 1)
count = 0


def dfs(vertex, days):
    global count

    if vertex == b:
        count += 1
        return

    if days == d:
        return

    visited[vertex] = True

    for next_vertex in graph[vertex]:
        if not visited[next_vertex]:
            dfs(next_vertex, days + 1)

    visited[vertex] = False


dfs(a, 0)

print(count)
