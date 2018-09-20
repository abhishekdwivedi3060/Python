import pyttsx3
import os
import time

def Speak_ICAO(str1,time_delay = 0.5):
    d = {
            'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo',
            'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett',
            'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar',
            'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
            'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee',
            'z':'zulu'
        }

    conv_string =  list(map(lambda x:d[x] ,str1.lower().replace(" ","")))
    print(conv_string)  
    engine = pyttsx3.init()
    for x in conv_string:
        engine.say(x)
        engine.runAndWait()
        time.sleep(time_delay)

str1 = input("Enter the String")
time_delay = int(input("Enter time delay in seconds"))
Speak_ICAO(str1,time_delay)



