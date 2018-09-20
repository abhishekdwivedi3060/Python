
from gen_n_char import generate_n_char

def histogram(list1, char):
    for x  in list1:
        generate_n_char(x, char)


n = int(input("Enter the list count"))
list2 = list()
print("Enter the list elements")
while n > 0:
    list2.append(int(input()))
    n -= 1
char = input("Enter the histogram character")
histogram(list2, char)
        


