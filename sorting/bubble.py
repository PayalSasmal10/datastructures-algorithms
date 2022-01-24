# bubble sort best case time complexity is O(n) when array is already sorted. 
# Here time complexity is O(n^2)


arr_list = [4,8,1,2,6,7]
def bubbleSort(arr):
    # Number of times it is passing 
    for times in range(len(arr)):
        
        # Largest part is storing at end and everytime we are ignoring which are already sorted
        for j in range(0,len(arr)-times-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)



bubbleSort(arr_list)






# def optimizeBubblesort(arr):
#     swapped = True
#     while(swapped):
#         swapped = False
#         for i in range(len(arr)-1):
#             if arr[i] > arr[i+1]:
#                 arr[i],arr[i+1] = arr[i+1], arr[i]
#                 swapped = True
#         print(arr)

# start = time()
# optimizeBubblesort(arr_list)
# end = time()-start
# print("optimized Bubble sort ends in "+ str(end) + "seconds")


