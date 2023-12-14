def uppercase_string(text):
    """docstring"""
    return text.upper()

def capitalize_words(string):
    """docstring"""
    words = string.split()  # Разделяем строку на список слов
    capitalized_words = [word.capitalize() for word in words]  # Делаем первую букву каждого слова заглавной
    result = " ".join(capitalized_words)  # Соединяем слова обратно в строку
    return result
