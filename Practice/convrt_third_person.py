def third_person(str1):
    if str1.endswith('y'):
        str1 = str1[:-1] + 'ies'
        return str1
    
    if str1.endswith('o' or 's' or 'x' or 'z'):
        str1 +=  'es'
        return str1
    
    if str1.endswith('ch' or  'sh'):
        str1 += 'es'
    else:
        str1 += 's'
    
    return str1


str1 = input("Enter the String ")
print(third_person(str1))
