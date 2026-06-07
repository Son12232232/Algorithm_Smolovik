n = int(input())
array = list(map(int, input().split()))

for i in range(1, n):
    current = array[i]
    j = i - 1
    changed = False

    while j >= 0 and array[j] > current:
        array[j + 1] = array[j]
        j -= 1
        changed = True

    array[j + 1] = current

    if changed:
        print(*array)
