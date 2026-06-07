import sys
import heapq

numbers = list(map(int, sys.stdin.buffer.read().split()))
heapq.heapify(numbers)
result = [heapq.heappop(numbers) for i in range(len(numbers))]
print(*result)
