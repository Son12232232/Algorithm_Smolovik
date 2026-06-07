import sys


class HashTable:
    """Хеш-таблиця з відкритою адресацією."""

    def __init__(self, expected_size):
        size = 1

        while size < expected_size * 2:
            size *= 2

        self.size = size
        self.mask = size - 1
        self.keys = [None] * size
        self.used = [False] * size

    def _hash(self, word):
        """Власна хеш-функція для рядків."""
        result = 0

        for symbol in word:
            result = (result * 131 + ord(symbol)) & 0xFFFFFFFFFFFFFFFF

        return result & self.mask

    def add(self, word):
        """Додає слово до таблиці."""
        index = self._hash(word)

        while self.keys[index] is not None:
            if self.keys[index] == word:
                return index

            index = (index + 1) & self.mask

        self.keys[index] = word
        return index

    def find(self, word):
        """Повертає індекс слова або -1, якщо слова немає."""
        index = self._hash(word)

        while self.keys[index] is not None:
            if self.keys[index] == word:
                return index

            index = (index + 1) & self.mask

        return -1

    def mark_as_used(self, word):
        """Позначає словникове слово як використане."""
        index = self.find(word)

        if index == -1:
            return False

        self.used[index] = True
        return True

    def all_words_used(self):
        """Перевіряє, чи всі слова зі словника були використані."""
        for index in range(self.size):
            if self.keys[index] is not None and not self.used[index]:
                return False

        return True


def check_word(word, vocabulary):
    if not word:
        return False

    return not vocabulary.mark_as_used(word)


def main():
    input_data = sys.stdin.buffer

    n, m = map(int, input_data.readline().split())
    vocabulary = HashTable(n)

    for _ in range(n):
        word = input_data.readline().decode().strip().lower()
        vocabulary.add(word)

    unknown_word_found = False

    for _ in range(m):
        line = input_data.readline().decode()
        current_word = []

        for symbol in line:
            if ("a" <= symbol <= "z") or ("A" <= symbol <= "Z"):
                current_word.append(symbol.lower())
            else:
                word = "".join(current_word)

                if check_word(word, vocabulary):
                    unknown_word_found = True

                current_word.clear()

        word = "".join(current_word)

        if check_word(word, vocabulary):
            unknown_word_found = True

    if unknown_word_found:
        print("Some words from the text are unknown.")
    elif not vocabulary.all_words_used():
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == "__main__":
    main()
