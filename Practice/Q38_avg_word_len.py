file_name = input("Enter the file name")
f = open(file_name)
list1 = str(f.read()).replace("\n"," ").replace("\t", " ").split(" ")
print(list1)
ch_count = 0
element_count = -1
for element in list1 :
    for ch in element:
        ch_count += 1
    element_count += 1

print(ch_count)
print(element_count)
print("the average word length is ",ch_count/element_count)

