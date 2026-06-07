import sys
sys.setrecursionlimit(5000)
quick_sort = lambda a: a if len(a) <= 1 else quick_sort([x for x in a if x < a[len(a) // 2]]) + [x for x in a if x == a[len(a) // 2]] + quick_sort([x for x in a if x > a[len(a) // 2]])
data = list(map(int, sys.stdin.buffer.read().split()))
n = data[0]
print(*quick_sort(data[1:n + 1]))
