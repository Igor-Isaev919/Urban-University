def all_variants(text):
    string = len(text)
    for i in range(1, string + 1):
        for j in range(string - i + 1):
            yield text[j:i + j]


if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)
