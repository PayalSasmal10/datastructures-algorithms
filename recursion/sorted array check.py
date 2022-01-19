# Write a function to check if the array is sorted or not
arr = [1,2,3,5,9]
n = len(arr)
i = 0
def isSortedArray(arr,i, n):
    if (i==n-1):
        return True
    
    if arr[i] < arr[i+1] and isSortedArray(arr,i+1,n):
        return True
    else:
        return False

print(isSortedArray(arr,i,n))

