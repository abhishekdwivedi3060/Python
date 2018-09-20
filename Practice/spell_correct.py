def correct(str1):
    str1 = str1.replace("  "," ").replace(".",". ")
    return str1


str1 = input("Enter the String ")
print(correct(str1))

