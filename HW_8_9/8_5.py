import sys


def bubble_sort_swap_count(array):
    swaps = 0
    n = len(array)

    for i in range(n - 1):
        was_swapped = False

        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 1
                was_swapped = True

        if not was_swapped:
            break

    return swaps


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))

    n = data[0]
    array = data[1:n + 1]

    print(bubble_sort_swap_count(array))


if __name__ == "__main__":
    main()
