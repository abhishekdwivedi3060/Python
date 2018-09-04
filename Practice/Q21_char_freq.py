def char_freq(str1):
    dict1 = dict()
    str1 = str1.replace(" ", "")
    
    for x in str1:
        if x in dict1:
            dict1[x] += 1
            
        else:
            dict1[x] = 1
    return dict1
  


if __name__ == "__main__":
    
    str1 = input("Enter the string")
    print(char_freq(str1))
