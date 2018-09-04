from check_member import is_member

def overlapping(list1, list2):
    for x in list1:
        if is_member(x, list2):
            return True
    return False        

if __name__ == "__main__"
list1 = list()
list2 = list()


count1 = int(input("Enter the number of elements of list1"))

while count1 > 0:
    list1.append(input())
    count1 -=1

count2 = int(input("Enter the number of elements of list2"))

while count2 > 0:
    list2.append(input())
    count2 -=1

print(overlapping(list1, list2))


