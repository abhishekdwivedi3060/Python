def reverse_string(s):
    c=0
    for x in s:
        c+=1
   
    c=c-1

    str1 = str()
    while c >=0:
        str1 += s[c]
        c -= 1
    return str1    

if __name__ == "__main__":
    s=input("enter the string ")
    print(reverse_string(s))
    print("Name: ", __name__)


