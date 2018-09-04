
def palindrome(s):
    pos=0
    for x in s:
        pos += 1
    print("The total characters are", pos)
    
    pos -= 1
    
    str1 = str()
    while pos >=0:
        str1 += s[pos]
        pos -= 1

    if s == str1:
        return True
    return False 


s=input("enter the string ")
print(palindrome(s))
