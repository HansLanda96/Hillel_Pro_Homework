from string import punctuation


def list_file(file_name: str) -> list:
    """
    :param file_name: file that u want to read and convert to list

    :return: list of words from text file without any punctuation marks
    """
    with open(file_name, 'r') as file:
        text = file.read().translate(str.maketrans('', '', punctuation)).split()
    return text


def text_file(file_name: str) -> str:
    """
    :param file_name: file that u want to read

    :return: initial text
    """
    with open(file_name, 'r') as file:
        file = file.read()
    return file


def dict_from_list(text: list) -> dict:
    """
    :param text: list of words from text

    :return: created dictionary where key is word and value is number of times word appears in text
    """
    keys = text
    values = [text.count(word) for word in keys]
    dictionary = dict(zip(keys, values))
    return dictionary


def max_value(dictionary: dict) -> str:
    """
    :param dictionary: dict

    :return: Returns word with max frequency appearance in text and times of appearance
    """
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    max_value_dict = max(values)
    max_key_dict = keys[values.index(max_value_dict)]
    return f'The most frequent word is {max_key_dict.capitalize()} and it appears {max_value_dict} times in text'


def main():
    print(f'\nText from file is: \n\n{text_file("long_text.txt")}'
          f'\n\nDictionary from text is: \n{dict_from_list(list_file("long_text.txt"))}'
          f'\n\n{max_value(dict_from_list(list_file("long_text.txt")))}')


if __name__ == '__main__':
    main()
