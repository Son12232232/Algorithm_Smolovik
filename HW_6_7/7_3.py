import sys


class HashTable:
    """Хеш-таблиця з відкритою адресацією."""

    def __init__(self, expected_size):
        size = 1

        # Завантаженість таблиці буде меншою за 50%
        while size < expected_size * 2:
            size *= 2

        self.table = [0] * size
        self.mask = size - 1
        self.count = 0

    def _hash(self, value):
        """Власна хеш-функція для номера телефону."""
        value ^= value >> 16
        value = (value * 0x45D9F3B) & 0xFFFFFFFF
        value ^= value >> 16

        return value & self.mask

    def add(self, value):
        """Додає значення, якщо його ще немає в таблиці."""
        index = self._hash(value)

        while self.table[index] != 0:
            if self.table[index] == value:
                return False

            index = (index + 1) & self.mask

        self.table[index] = value
        self.count += 1
        return True


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))

    n = data[0]
    contacts = HashTable(n)

    for i in range(1, n + 1):
        contacts.add(data[i])

    print(contacts.count)


if __name__ == "__main__":
    main()
