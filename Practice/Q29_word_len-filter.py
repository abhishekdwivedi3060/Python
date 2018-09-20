def filter_long_words(word_list,n):
    return list(filter(lambda word: len(word) > n, word_list))


n = int(input("Enter the word length"))
count = int(input("Enter the count of list"))
word_list = [input() for x in range(0, count)]
print(filter_long_words(word_list, n))
