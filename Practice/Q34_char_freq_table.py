from Q21_char_freq import char_freq

def char_freq_table(file_name):
    f = open(file_name)
    return char_freq(f.read().replace("\n",""))


file_name = input("Enter the file name")
print(char_freq_table(file_name))
            

        
