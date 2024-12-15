class WordsFinder:
    def __init__(self, *args):
        self.name = list(args)

    def get_all_words(self):
        all_words = {}
        for x in self.name:
            with open(x, encoding="utf-8") as file:
                words = file.read().lower()
                for i in words:
                    if i in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        words = words.replace(i, '')
                words = list(words.split())
            all_words[x] = words
        return all_words

    def find(self, word):
        d = {}
        for key, value in self.get_all_words().items():
            for i in value:
                if i == word.lower():
                    d[key] = value.index(i) + 1
                    break
        return d

    def count(self, word):
        d = {}
        for key, value in self.get_all_words().items():
            d[key] = value.count(word.lower())
        return d


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
