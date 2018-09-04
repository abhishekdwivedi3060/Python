def make_ing_form(word):
    consonant = "bcdfghjklmnpqrstvwxyz"
    if word == "":
        print("No word entered ")
    elif word.endswith('ie'):
        word = word[:-2] + 'ying'
        return word

    if word.endswith('e'):
         word = word[:-1] + 'ing'
         return word

    if len(word) >= 3 and word[len(word)-3] in consonant and word[len(word)-2] not in consonant and word[len(word)-1] in consonant:
        word += word[len(word)-1] + 'ing'
    else:
        word += 's'
    return word


word = input("Enter the word ")
print(make_ing_form(word))         
