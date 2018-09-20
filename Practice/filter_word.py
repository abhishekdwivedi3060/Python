from len import  len

def filter_long_words(list1, n):
    list2 = list()

    for x in list1:
       if len(x) > n:
           list2.append(x)
    return list2


count = int(input("Enter the list count"))
n = int(input("Enter the number of character count"))
list1 = list()
print("enter the list elements")
while count > 0:
    list1.append(input())
    count -= 1
print(list1)
print(filter_long_words(list1, n))
