# Find the decimal of binary.
# Input: 1 0 0 0
# output: 8

def binarytodecimal(binary):
    decimal,i = 0,0
    while(binary!=0):
        module_dec = binary % 10
        decimal = decimal + module_dec * pow(2, i)
        binary = binary // 10
        i += 1
    print(decimal)

binarytodecimal(1011)