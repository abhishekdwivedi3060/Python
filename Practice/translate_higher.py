def translate(word_list):
    dict1 = {
                "merry":"god",
                "christmas":"jul",
                "and":"och",
                "happy":"gott",
                "new":"nytt",
                "year":"år"
            }
    return list(map(lambda word: dict1[word], word_list))


word_list =  input("Enter the English words").lower().split(" ")
print("In Swedish ", translate(word_list))
