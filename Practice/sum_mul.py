def sum(list1):
    sum=0
    for x in list1:
        sum+=x
    print("the sum is",sum)
def mul(list1):
    pro=1
    for x in list1:
        pro*=x
    print("the product is ",pro)

count=int(input("Enter the number of list elements"))
list2=list()
while count > 0:
    x=int(input())
    list2.append(x)
    count -=1
sum(list2)
mul(list2)
