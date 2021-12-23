# find out the subarray

def subarray(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print()
            for k in range(i,j+1):
                print(arr[k],end=',')
            

subarray([-2,3,4,-1,5,-12,6,1,3])