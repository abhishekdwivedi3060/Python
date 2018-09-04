
try:
    def maxof2(a,b):

        if a > b:
            print("a is greater")
        elif a == b:
            print("a and b are equal")
        else:
            print("b is greater")

    a=int(input())
    b=int(input())
    print(a,b)
    maxof2(a,b)
 
except ValueError:
    print("error...enter int type only")

  

