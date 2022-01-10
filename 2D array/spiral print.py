# https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
# Input:  1    2   3   4
#         5    6   7   8
#         9   10  11  12
#         13  14  15  16
# Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
]
row,col =4,4

def spiralprint(arr,row,col):
    startrow = 0
    endcol = col - 1
    endrow = row - 1
    startcol = 0

    while(startcol <= endcol and startrow <=endrow):
        # start row
        for srow in range(startcol,endcol+1):
            print(arr[startrow][srow])
        # end col
        for ecol in range(startrow+1, endrow+1):
            print(arr[ecol][endcol])
        # end row
        for erow in range(endcol-1,startcol-1,-1):
            if startrow == endrow:
                
                break
            print(arr[endrow][erow])
        # startcol
        for scol in range(endrow-1, startrow,-1):
            if startcol == endcol:
                break
            print(arr[scol][startcol])
        
        #update the variables to point to inner spiral
        startrow += 1
        startcol += 1
        endrow -= 1
        endcol -= 1

spiralprint(arr, row, col)