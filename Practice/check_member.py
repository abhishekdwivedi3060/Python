def is_member(key,list1):
    for x in list1:
        if x == key:
            return True
    return False

list1 = list()

if __name__ == "__main__":
    count = int(input("Enter the number of elements"))

    while count > 0:
        list1.append(input())
        count -=1

    key = input("Enter the key to search")

    print(is_member(key, list1))

    
