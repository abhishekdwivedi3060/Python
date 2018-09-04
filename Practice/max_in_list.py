clsdef max_in_list(list1):
    maxm = list1[0]
    for x in list1:
        if x > maxm:
            maxm = x
    return maxm


if __name__ == "__main__":
    n=int(input("Enter the list count"))
    list1 = list()
    print("enter the list elements")
    while n > 0:
        list1.append(int(input()))
        n -= 1
    print("maximum number is", max_in_list(list1))   
