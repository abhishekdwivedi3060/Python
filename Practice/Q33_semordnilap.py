from rev import reverse_string
def semordnilap(file_name):
    f = open(file_name)
    res = {}
    for line in f:
        for line1 in f:
            if line.strip() == line1.strip():
                res.add(line.strip()+" "+line1.strip())
    return res

file_name = input("Enter the file name")
print(semordnilap(file_name))
            
