# Find the binary of decimal.
# Input: 8
# output: 1 0 0 0

def decimaltobinary(n):
    if n>=1:
        decimaltobinary(n//2)
    
        print(n%2, end=" ")
    

decimaltobinary(8)
