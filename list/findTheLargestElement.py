# Implement a function that takes array of integers as input and returns the largest element.
# sorted or sort function time complexity is o(nlogn)
class largestElement:
    def largestelementofaList(arr):
        ls = sorted(arr)
        print(ls[len(arr)-1])


le = largestElement
le.largestelementofaList([-1,-2,-3,-3,8])

# optimize this. O(n) time complexity

def largestEelement(arr):
    largestNumber = 0
    for i in arr:
        largestNumber = max(largestNumber,i)
    return largestNumber[-1,-2,-3,-3,8]


print(largestEelement([-1,-2,-3,-3,8]))






