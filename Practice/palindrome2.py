from rev import reverse_string as revs

def palindrome(s):

    if revs(s) == s:
        return True
    return False 

if __name__ == "__main__":
    s=input("enter the string to check: ")
    print(palindrome(s))
