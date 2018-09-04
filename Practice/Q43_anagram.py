import urllib.request 
from Q21_char_freq import char_freq

word_list = urllib.request.urlopen("http://www.puzzlers.org/pub/wordlists/unixdict.txt") # it's a file like object and works just like a file
print(word_list.read())
"""list1 = []
for line in str(word_list): # files are iterable
    list1.append(char_freq(line))

print(list1)"""
