def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)
    return same_words
result = single_root_words("game", "Gamer", "GAMEFUL", "endgame", "gamewise")
print(f'Найдены однокоренные слова: {' '.join(result)}')