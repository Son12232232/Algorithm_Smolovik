LIMIT = 16384
def karatsuba(a, b): return 0 if a == 0 or b == 0 else a * b if min(a.bit_length(), b.bit_length()) <= LIMIT else ((m := max(a.bit_length(), b.bit_length()) // 2), (mask := (1 << m) - 1), (a0 := a & mask), (a1 := a >> m), (b0 := b & mask), (b1 := b >> m), (z0 := karatsuba(a0, b0)), (z2 := karatsuba(a1, b1)), (z1 := karatsuba(a0 + a1, b0 + b1)), (z2 << (2 * m)) + ((z1 - z2 - z0) << m) + z0)[-1]
a_text, b_text = sys.stdin.buffer.readline().split()
a = int(a_text)
b = int(b_text)
print(karatsuba(a, b))
