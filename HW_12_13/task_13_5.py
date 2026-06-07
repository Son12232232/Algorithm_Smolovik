import sys


def is_correct(sequence):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for bracket in sequence:
        if bracket in "([{":
            stack.append(bracket)
        else:
            if not stack or stack[-1] != pairs[bracket]:
                return False
            stack.pop()

    return len(stack) == 0


sequence = sys.stdin.readline().strip()

if is_correct(sequence):
    print("yes")
else:
    print("no")
