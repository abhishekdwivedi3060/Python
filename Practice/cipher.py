def caesar_cipher(str1):
    dict1 = {
            'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
            'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
            'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
            'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
            'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
            'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
            'W':'J', 'X':'K', 'Y':'L', 'Z':'M'
        }
    str2 = ""
    for x in str1:
        if x == " ":
            str2 += " "
        else:
            str2 += dict1.get(x,"key not found")

    return str2
         


str1 = input ("Enter the String ")
print(caesar_cipher(str1))
