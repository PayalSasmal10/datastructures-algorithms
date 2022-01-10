# Find the binary of decimal.
# Input: 8
# output: 1 0 0 0

def decimaltobinary(n):
    if n>1:
        n = n//2
    else:
        n = n%2
    return n

print(decimaltobinary(8))
