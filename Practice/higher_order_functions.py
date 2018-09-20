def map(func, data_seq):
    list1 = []
    for x in data_seq:
       list1.append(func(x))
    return list1


def filter(func, data_seq):
    list1 = []
    for x in data_seq:
       if func(x):
           list1.append(x)
    return list1


def reduce(func, data_seq):
    if len(data_seq) == 0:
        return
    if len(data_seq) == 1:            
        return data_seq[0]
    res = int()

    for x in range(len(data_seq)-1):
        if x == 0:
            res = func(data_seq[x], data_seq[x+1])
        
        else:
            res = func(res, data_seq[x+1])
    return res

square = lambda num: num**2
maximum = lambda num:num >0
sum = lambda x,y: x+y

list2 = [2,4,5,6,7]

print(map(square, list2))
print(filter(maximum, list2))
print(reduce(sum, list2))
