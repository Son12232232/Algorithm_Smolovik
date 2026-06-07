from functools import reduce
n, k = map(int, input().split())
permutations = reduce(lambda current, _: [p + (number,) for p in current for number in range(1, n + 1) if number not in p], range(k), [()])
print("\n".join(" ".join(map(str, p)) for p in permutations))
