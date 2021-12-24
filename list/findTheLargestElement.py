#Implement a function that takes array of integers as input and returns the largest element.
# sorted function time complexity is o(n logn)
class largestElement:
    def largestelementofaList(arr):
        ls = sorted(arr)
        print(ls[len(arr)-1])


le = largestElement
le.largestelementofaList([-1,-2,-3,-3,8])

