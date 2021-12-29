# insertion sort time complexity for sorted array is O(n)
# for unseorted arry, it is O(n^2)
from time import time

# arr_list = [-2, 3, 4, -1, 5, -12, 6, 1, 3]
arr_list = [5,3,2,1,6]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        
        prv = i-1
        current_number = arr[i]
        while(prv >= 0 and arr[prv] > current_number):
            arr[prv+1] = arr[prv]
            prv = prv - 1
        arr[prv+1] = current_number
        print(arr)


start = time()
insertion_sort(arr_list)
end = time()-start

print("insertion sort time taken " + str(end) + " seconds")


