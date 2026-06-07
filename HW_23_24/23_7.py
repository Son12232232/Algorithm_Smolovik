import sys

input = sys.stdin.buffer.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
components = []

for start in range(1, n + 1):
    if not visited[start]:
        component = []
        stack = [start]
        visited[start] = True

        while stack:
            vertex = stack.pop()
            component.append(vertex)

            for next_vertex in graph[vertex]:
                if not visited[next_vertex]:
                    visited[next_vertex] = True
                    stack.append(next_vertex)

        components.append(component)

answer = [str(len(components))]

for component in components:
    answer.append(str(len(component)))
    answer.append(" ".join(map(str, component)))

print("\n".join(answer))
