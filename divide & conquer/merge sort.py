
# merge 2 arrays
def mergearrays(array,s,e):
    i = s
    m = (s+e)//2
    j = m+1
    temp = []
    while(i<=m and j <=e):
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
        
    # copy remaining elements from first array
    while(i<=m):
        temp.append(array[i])
        i += 1

    # copy remaining elements from the second array
    while(j<=e):
        temp.append(array[j])
        j += 1
        
    # copy back to the original array
    t = 0
    for k in range(s,e+1):
        array[k] = temp[t]
        t += 1
    return

# sort the array
def mergeSort(arr,s,e):
    if (s>=e):
        return

    mid = (s+e) // 2
    mergeSort(arr,s,mid)
    mergeSort(arr,mid+1,e)
    return mergearrays(arr,s,e)

if __name__ == "__main__":
    arr = [10,5,2,11,7,4,3]
    s= 0
    e = len(arr)-1
    mergeSort(arr,s,e)
    for y in arr:
        print(y)
    

