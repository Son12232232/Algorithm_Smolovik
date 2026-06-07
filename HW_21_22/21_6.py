n, m = map(int, input().split())

in_degree = [0] * n
out_degree = [0] * n

for _ in range(m):
    start, end = map(int, input().split())

    out_degree[start - 1] += 1
    in_degree[end - 1] += 1

for i in range(n):
    print(in_degree[i], out_degree[i])
