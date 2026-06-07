import math


def f(x):
    return math.sin(x) - x / 3


left = 1.6
right = 3.0

# Метод бісекції
for _ in range(100):
    middle = (left + right) / 2

    if f(left) * f(middle) <= 0:
        right = middle
    else:
        left = middle

x = (left + right) / 2

print(f"x = {x:.10f}")


# Відповідь: x ≈ 2.2788626601

