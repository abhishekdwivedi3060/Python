input_string = input("Enter the bracket String")
flag = False
x =0
while x < len(input_string)-1:
    if input_string[x] == '[' and input_string[x+1] == ']':
        flag = True 
       
    else:
        flag = False
    x += 1
if flag:
    print("ok")
else:
    print("not ok")
