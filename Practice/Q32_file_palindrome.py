from palindrome2 import palindrome

def palindrome_line(file_name):
    f = open(file_name,"r")
    for line in f:
        if palindrome(line.strip()):
            print(line) 
    f.close()
if __name__ == "__main__":
    file_name = input("Enter the file name")
    palindrome_line(file_name)


