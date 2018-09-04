
from len import len

def find_longest_word(list1):
      maxm = len(list1[0])
    for x in list1:
        if len(x) > maxm
        max = len(x)

        



if __name__ == "__main__":
    n = int(input("Enter the list elements"))
    list1 = list()
    print("Enter the elements")
    while n > 0:
        list1.append(input())
        n -= 1

print("The largest word length is ", find_longest_word(list1))
