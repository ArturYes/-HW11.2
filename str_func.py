def uppercase_string(text):
    """функция  заглавные буквы"""
    return text.upper()

def capitalize_words(string):
    """делает заглавной буквой каждого слова"""
    words = string.split()  # Разделяем строку на список слов
    capitalized_words = [word.capitalize() for word in words]  # Делаем первую букву каждого слова заглавной
    result = " ".join(capitalized_words)  # Соединяем слова обратно в строку
    return result
