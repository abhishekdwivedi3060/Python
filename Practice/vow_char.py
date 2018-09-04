def vow_char(s):
    vow=['a','e','i','o','u','A','E','I','O','U']
    for x in vow:
        if x==s:
            return True
    return False    
s=str(input())
print(vow_char(s))
