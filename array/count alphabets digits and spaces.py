# Given sentence, count the number of alphabets, digits & spaces

test = "payalsasmal 4387"

def alphabets(ch):
    alph = 0
    digits = 0
    spaces = 0
    for i in ch:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            alph += 1
        elif (i>='0' and i<='9'):
            digits += 1
        elif (i==' ') or (i=='\t'):
            spaces += 1
    print("Total alphabets :", alph)
    print("Total digits :", digits)
    print("Total spaces :", spaces)

alphabets(test)
