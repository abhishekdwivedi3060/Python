print("Enter the Word")
while True:
    word = input("\n")
    hidden_word = "snake"
    print("Clue:",end="")
    for ch in word:
        if ch in hidden_word:
            if word.index(ch) == hidden_word.index(ch):
                print("["+ ch +"]",end="")
            else:
                print("(" + ch + ")",end="")
        else:
            print(ch,end="")       
    if word == hidden_word:
        break
