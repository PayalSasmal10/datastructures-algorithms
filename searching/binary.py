def binarySearch(arr,key):
    s =0
    e = len(arr) - 1

    while(s<=e):
        mid = (s+e)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            e = mid - 1
        else:
            s = mid+1
    return -1


print("Index of the key is",binarySearch([90,50,45,38,9], 45))


