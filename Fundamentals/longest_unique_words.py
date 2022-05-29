def get_n_longest_unique_words(words, n):
    unique = []
    for word in words:
        if words.count(word) == 1:
            unique.append(word)
    unique.sort(key=len)
    return unique[-1:-1-n:-1]




words = [
            "Hello",
            "AlgoExpert",
            "Algo",
            "Testing",
            "Programming",
            "Programming",
            "Coding",
            "Python",
            "JavaScript",
            "Coding",
            "Ruby",
        ]
n = 5

print(get_n_longest_unique_words(words, n))