from time import time
arr_list = [1,2,3,4,5]
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                print(arr)


start = time()
bubbleSort(arr_list)
end = time()-start
print("Bubble sort ends in "+ str(end) + "seconds")


def optimizeBubblesort(arr):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
                swapped = True
        print(arr)

start = time()
optimizeBubblesort(arr_list)
end = time()-start
print("optimized Bubble sort ends in "+ str(end) + "seconds")


