# arr[1,2,3,4], pair-(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)
def printallpairs(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            pair = (arr[i],arr[j])
            print(pair)

printallpairs([1,2,3,4])



