# find out the subarray

def subarray(arr):
    for i in range(len(arr)):
        for j in range(len(arr)+1):
            print()
            for k in range(i,j):
                print(arr[k],end=',')
            

subarray([10,89,65,78,60])