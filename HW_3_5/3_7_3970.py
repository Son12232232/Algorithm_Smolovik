import sys
from bisect import bisect_left, bisect_right

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n+1]]
    
    m = int(input_data[n+1])
    queries = [int(x) for x in input_data[n+2 : n+2+m]]
    
    result = []
    for q in queries:
        left = bisect_left(arr, q)
        right = bisect_right(arr, q)
        result.append(str(right - left))
        
    sys.stdout.write('\n'.join(result) + '\n')

if __name__ == '__main__':
    solve()
