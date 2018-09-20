def translate(string_words, lexicon_words):
    ans = []
    for word in string_words:
            ans.append(lexicon_words.get(word, "not a valid lexicon"))
    return ' '.join(ans)


str1 = input("Enter the English String ").lower().split(" ")

words = {   
            "merry":"god",
            "christmas":"jul",
            "and":"och",
            "happy":"gott",
            "new":"nytt",
            "year":"ar"
        }

print(translate(str1, words))



