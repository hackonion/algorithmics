# Link https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example

alphabet_position("The sunset sets at twelve o' clock.")

Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
"""
test = "The sunset sets at twelve o' clock."

def clean_text(text:str):
    
    clean_leter = text.lower().replace("/|!|,|","").replace("'","").replace(" ","").replace(".","")
        
    return clean_leter


def remplace(text:str):
    
    list_numbers = {"a":1,"b":2, "c":3, "d":4,"e":5, "f":6, "g":7, "h":8,
                "i":9, "j":10, "k":11, "l":12, "m":13, "n":14,"o":15,
                "p":16, "q":17, "r":18, "s":19, "t":20,"u":21, "v":22, 
                "w":23, "x":24, "y":25, "z":26}
    arr = []
    separator = " "
    for i in clean_text(text):
        if i in list_numbers: 
            arr.append(str(list_numbers[i]))
    return str(separator.join(arr))


test = "The sunset sets at twelve o' clock."
remplace(test)