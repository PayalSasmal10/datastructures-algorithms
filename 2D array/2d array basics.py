# create a 2d array  

# class twoDimensionalArray:
arr= []
# def twoDArray(arr, row, column):
#     for i in range(row):
#         for j in range(column):
#             print(arr[i][j])
    
def takeinput():
    row = int(input())
    column = int(input())
    for r in range(row):
        inner = []
        for c in range(column):
            newInput = int(input())
            inner.append(newInput)
        arr.append(inner)
    for k in arr:
        print(k, sep="\n")
        
    # twoDArray(arr, row, column)


takeinput()

# object_2dArray = twoDimensionalArray
# object_2dArray.takeinput()
