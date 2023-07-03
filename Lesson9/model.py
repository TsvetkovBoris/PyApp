import json

phones_book = {}
path = 'phones.json'


def open_file():
    global phones_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phones_book = json.load(file)
        return True
    except:
        return False


def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phones_book, file, ensure_ascii=False)
        return True
    except:
        return False


def search(word: str) -> dict[int: dict[str, str]]:
    result = {}
    for index, contact in phones_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result


def check_id():
    if phones_book:
        return max(list(map(int, phones_book))) + 1
    return 1


def add_contact(new: {int: dict[str, str]}):
    contact = {check_id(): new}
    phones_book.update(contact)


def delete(word) -> dict[int: dict[str, str]]:
    save_file()

    phones_book.pop(str(list(dict(word).keys())[0]))
    save_file()


def change(word, temp) -> dict[int: dict[str, str]]:

    contact = {list(word.keys())[0]: temp}
    phones_book.update(contact)
