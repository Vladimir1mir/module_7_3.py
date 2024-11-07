class WordsFinder:
    def __init__(self, *file_names):  # инициализирую объект, принимаю список
        self.file_names = file_names  # неограниченное кол-во названий файлов

    def get_all_words(self):
        all_words = {}  # пустой словарь для хранения
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']  # пунктуация (список) для удаления
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:  # открыл для чтения
                content = file.read().lower()  # читаем содержимое и привожу в нижний регистр
                for punct in punctuation:  # удаляю знаки пунктуации из текста
                    content = content.replace(punct, '')
                words = content.split()
                all_words[file_name] = words
        return all_words # возвращаю словарь

    def find(self, word):
        places = {} # пустой словарь
        for key, value in self.get_all_words().items(): # циклом перебираю улюч и значение из словаря метода get_all_words
            if word.lower() in value:
                places[key] = value.index(word.lower()) + 1 # для корректности позиция начинается с единицы
        return places

    def count(self, word):
        counter = {}  # пустой словарь
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counter[value] = words_count
        return counter


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
