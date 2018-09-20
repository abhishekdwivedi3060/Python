title_list = ['Mr.:', 'Mrs.', 'Dr.', 'Jr.']
file_name = input("Enter the file_name")
f = open(file_name, 'r+')
string = str(f.read()).replace("\n", " ")
string = string.replace("?", "?\n").replace("!", "!\n")
for c, ch in enumerate(string):
    if ch == '.' and string[c+1] == " " :
         print(string[c-2:c+1])
         if string[c-2:c+1] not in title_list or string[c-3:c+1] not in title_list:
             string.replace(string[c+1],"\n")


print(string)
