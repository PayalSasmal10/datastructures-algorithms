# Given an array of integers  ( sorted) and integer Val.Implement a function that takes A 
# and Val as input parameters and returns the lower bound of Val. ex- A =[-1,-1,2,3,5] Val=4
# Ans=3. As 3 is smaller than 4

def lowerBound(arr, key):
    s = 0
    e = len(arr)
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == key:
            arr[mid] = key
        elif arr[mid] < key:
            s = mid + 1
        else:
            e = mid - 1
    return arr[mid]


print(lowerBound([-1,-1,2,3,5], 4))


