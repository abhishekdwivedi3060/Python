def generate_n_char(n, str1):
    str2 = str()
    while n > 0:
        str2 += str1
        n -= 1
    print(str2)


if __name__ == "__main__":
    n = int(input("Enter the multiplication number"))
    str1 = input("Enter the string")
    generate_n_char(n, str1)
