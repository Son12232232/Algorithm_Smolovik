import sys

prefix = sys.stdin.readline().strip()

priority = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2
}

operators = "+-*/"
stack = []

for symbol in reversed(prefix):
    if symbol not in operators:
        stack.append((symbol, 3))
    else:
        left_expression, left_priority = stack.pop()
        right_expression, right_priority = stack.pop()

        current_priority = priority[symbol]

        if left_priority < current_priority:
            left_expression = "(" + left_expression + ")"

        if right_priority < current_priority:
            right_expression = "(" + right_expression + ")"
        elif right_priority == current_priority and symbol in "-/":
            right_expression = "(" + right_expression + ")"

        expression = left_expression + symbol + right_expression
        stack.append((expression, current_priority))

print(stack[-1][0])
