# Завдання 6.3

_EMPTY = 0
_USED = 1
_DELETED = 2

_table = []
_count = 0
_deleted = 0


def _hash_string(text):
    """Власна хеш-функція для рядка."""
    value = 0

    for symbol in text:
        value = (value * 131 + ord(symbol)) & 0x7FFFFFFFFFFFFFFF

    return value


def _find_slot(author, for_insert=False):
    """Пошук позиції методом лінійного пробування."""
    size = len(_table)
    index = _hash_string(author) % size
    first_deleted = -1

    for _ in range(size):
        state, stored_author, books = _table[index]

        if state == _EMPTY:
            if for_insert and first_deleted != -1:
                return first_deleted

            return index

        if state == _DELETED:
            if for_insert and first_deleted == -1:
                first_deleted = index

        elif stored_author == author:
            return index

        index = (index + 1) % size

    return first_deleted


def _resize(new_size):
    """Збільшення хеш-таблиці."""
    global _table, _count, _deleted

    old_table = _table

    _table = [
        [_EMPTY, None, None]
        for _ in range(new_size)
    ]

    _count = 0
    _deleted = 0

    for state, author, books in old_table:
        if state == _USED:
            index = _find_slot(author, True)
            _table[index] = [_USED, author, books]
            _count += 1


def init():
    """Викликається один раз на початку роботи програми."""
    global _table, _count, _deleted

    _table = [
        [_EMPTY, None, None]
        for _ in range(17)
    ]

    _count = 0
    _deleted = 0


def addBook(author, title):
    """Додає книгу до бібліотеки."""
    global _count, _deleted

    # Збільшуємо таблицю, якщо вона заповнена приблизно на 70%.
    if (_count + _deleted + 1) * 10 >= len(_table) * 7:
        _resize(len(_table) * 2 + 1)

    index = _find_slot(author, True)

    if index == -1:
        _resize(len(_table) * 2 + 1)
        index = _find_slot(author, True)

    state, stored_author, books = _table[index]

    # Автор уже є у таблиці.
    if state == _USED:
        # Не додаємо однакову книгу двічі.
        for book in books:
            if book == title:
                return

        books.append(title)
        return

    if state == _DELETED:
        _deleted -= 1

    # Додаємо нового автора.
    _table[index] = [_USED, author, [title]]
    _count += 1


def find(author, title):
    """Перевіряє, чи є книга у бібліотеці."""
    index = _find_slot(author)

    if index == -1 or _table[index][0] != _USED:
        return False

    books = _table[index][2]

    for book in books:
        if book == title:
            return True

    return False


def delete(author, title):
    """Видаляє книгу з бібліотеки."""
    global _count, _deleted

    index = _find_slot(author)

    if index == -1 or _table[index][0] != _USED:
        return

    books = _table[index][2]

    for i in range(len(books)):
        if books[i] == title:
            books.pop(i)

            # Якщо в автора більше немає книг,
            # позначаємо комірку як видалену.
            if len(books) == 0:
                _table[index] = [_DELETED, None, None]
                _count -= 1
                _deleted += 1

            return


def findByAuthor(author):
    """Повертає книги автора в алфавітному порядку."""
    index = _find_slot(author)

    if index == -1 or _table[index][0] != _USED:
        return []

    return sorted(_table[index][2])

