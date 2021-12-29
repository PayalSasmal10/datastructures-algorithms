# Given an integer vector and bool variable flag, your task is to sort the vector
# accordance to the boolean value. If the boolean value passed is true then sort it in
# non-decreasing order or vice versa.
import time
arr_list = [111, 33, 5, 7, 29]

def sortwithcomparator(arr, flag):
    while(flag):
        flag = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                  arr[i],arr[i+1] = arr[i+1],arr[i]
                  flag = 1
                
    return arr


print(sortwithcomparator(arr_list,1))





