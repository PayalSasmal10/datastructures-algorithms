# 1st way: o(n)
# def reverselist(arr):
#     print(arr[::-1])


#reverselist([8,4,6,90])

# 2nd way:o(n)
# def reverselist(arr):
#     arr.reverse()
#     print(arr)


# reverselist([8,4,6,90])

#3rd way:o(n)
# def reverselist(arr):
#     for i in reversed(arr):
#         print(i)

# reverselist([8,4,6,90])

# 4th way: o(n)
# This scenario is possible if the array is in sorted order
def reverselist(arr):
    s = 0
    e = len(arr)-1
    while(s<e):
        arr[s],arr[e]=arr[e],arr[s]
        s += 1
        e -= 1
    return arr
       


print(reverselist([10,20,30,45,87]))