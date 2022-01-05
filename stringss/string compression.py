# input = ["a", "a", "b", "b", "c", "c", "c"]
# o/p = a2b2c3

string_chr = ["a", "a", "b", "b", "c", "c", "c"]

def stringCompression(string_chr):
    newString = ''
    count = 1

    for i in range(len(string_chr)-1):
        print(i)
        print(string_chr[i])
        if string_chr[i] == string_chr[i+1]:
            count += 1
        else:
            newString += string_chr[i]+str(count)
            count = 1
        
        if i == len(string_chr)-2:
            newString += string_chr[i]+str(count)

        i += 1      
        
    return newString


print(stringCompression(string_chr))
