import string

set2 = set(string.ascii_lowercase)

def panag(s, set2):
    s.replace(" ","")
    set1 = set(s.lower())
    if set1 == set2:
        return True
    return False


s = input("Enter the string")
print(panag(s, set2))

