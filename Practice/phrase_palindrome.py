from rev import reverse_string
def phrase_palin(str1):
    str1 = str1.replace(" ","").replace("?","").replace(",","").replace("'","")
    str2 = reverse_string(str1)
    if str2 == str1:
        return True
    return False

if __name__ == "__main__":
    str1 = input("Enter the String")
    print(phrase_palin(str1))
