import sys


def can_reorder(n, required_order):
    stack = []
    next_car = 1

    for required_car in required_order:
        # Заганяємо вагони на станцію, доки потрібний вагон
        # не опиниться на вершині стека.
        while next_car <= n and (
            not stack or stack[-1] != required_car
        ):
            stack.append(next_car)
            next_car += 1

        # Якщо потрібний вагон зверху, відправляємо його в напрямку B.
        if stack and stack[-1] == required_car:
            stack.pop()
        else:
            return False

    return True


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    index = 0
    answers = []

    while index < len(data):
        n = data[index]
        index += 1

        if n == 0:
            break

        while index < len(data):
            first_car = data[index]
            index += 1

            # Нуль завершує поточний блок.
            if first_car == 0:
                break

            required_order = [first_car]

            for _ in range(n - 1):
                required_order.append(data[index])
                index += 1

            if can_reorder(n, required_order):
                answers.append("Yes")
            else:
                answers.append("No")

        # Порожній рядок після кожного блоку.
        answers.append("")

    print("\n".join(answers))


if __name__ == "__main__":
    main()
