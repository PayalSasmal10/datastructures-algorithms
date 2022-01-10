# find 4 exists in array or not.
# Linear serach means serach the element until unless it get that
# o(n) time complexity
class linearSearch:
    
    def findthenumber(arr, target):
        for i in arr:
            if i == target:
                return i
        return -1

leanrSearchObj = linearSearch
print(leanrSearchObj.findthenumber([2,5,8,7,4,5], 3))