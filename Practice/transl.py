def transl(s):
    vow=['a','e','i','o','u','A','E','I','O','U']
    pos=0
    str1=str()
    for x in s:
        for y in vow:
            if x==y:
                str1[pos]=s[pos]
                pos += 1
                break

        str1[pos]=s[pos]
        str1[pos+1]="o"
        str1[pos+1]=s[pos]
        pos+=3
    print(str1)        
s=input("Enter the string")
transl(s)
