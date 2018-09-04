from functools import reduce
from max_of_list_reduce import max_of_list

def longest_word(word_string):
   return max_of_list(list(map(lambda s:len(s),word_string)))


if __name__ == "__main__":
    n =int(input("Enter the number of list elements" ))
    word_string = [input() for x in range(0,n) ]
    print("The longest length is ", longest_word(word_string))


