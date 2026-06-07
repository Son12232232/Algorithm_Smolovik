n, m = map(int, input().split())

edges = set()

for _ in range(m):
    u, v = map(int, input().split())

    if u != v:
        edges.add((min(u, v), max(u, v)))

required_edges = n * (n - 1) // 2

if len(edges) == required_edges:
    print("YES")
else:
    print("NO")
