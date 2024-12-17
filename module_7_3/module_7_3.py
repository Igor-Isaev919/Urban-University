class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read().lower()

                punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for punct in punctuation:
                    content = content.replace(punct, ' ')

                words = content.split()
                all_words[file_name] = words

        return all_words


    def find(self, word):
        result = {}
        word = word.lower()

        for file_name, words in self.get_all_words().items():
            if word in words:
                result[file_name] = words.index(word) + 1

        return result

    def count(self, word):
        result = {}
        word = word.lower()

        for file_name, words in self.get_all_words().items():
            count = words.count(word)
            if count >= 0:
                result[file_name] = count

        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))