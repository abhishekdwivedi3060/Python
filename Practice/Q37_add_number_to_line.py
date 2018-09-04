file_name = input("enter the file name")
f = open(file_name)
count = 1
f1 = open("eg.txt","w+")
for line in f:
   f1.write(str(count)+"\t"+line)
   count += 1
f.close()
#f1.close()
#f1 = open("eg.txt")
f1.seek(0,0)
print(f1.read())
f1.close()
