def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                print(arr)


bubbleSort([-2,3,4,-1,5,-12,6,1,3])