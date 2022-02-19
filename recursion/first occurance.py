# Print index of the first occurance of the value.

arr = [2,5,7,89,2]
i = 0
key = 10
def firstoccurance(arr,i,key):
    # if i == 0:
    #     return -1
    if arr[i] == key:
        return i
    elif i == len(arr) -1:
        return -1
    return firstoccurance(arr,i+1,key)
    

print(firstoccurance(arr,i,key))

