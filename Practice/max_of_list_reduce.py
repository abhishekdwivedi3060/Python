from functools import reduce

def max_of_list(num_list):
    return reduce(lambda x, y: x if x > y else y,num_list)


if __name__ == "__main__":
    n = int(input("Enter the number of list elements" ))
    num_list = [int(input()) for x in range(0,n) ]
    print("The highest number is ",max_of_list(num_list))

      
