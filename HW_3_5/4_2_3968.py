import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    C = float(input_data[0])
    
    left = 0.0
    right = max(1.0, C)
    for _ in range(100):
        mid = (left + right) / 2.0
        val = mid * mid + math.sqrt(mid)
        
        if val < C:
            left = mid
        else:
            right = mid

    sys.stdout.write(f"{left:.6f}\n")

if __name__ == '__main__':
    solve()
