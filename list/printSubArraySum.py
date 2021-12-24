#Find out the largest sum of sub array suppose -2,3,4 = 5 
# O(n^3)using Brute Force Algo
class A:
    
    def printSubArraySum(arr):
        largestSum = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                currentSum = 0
                for k in range(i,j+1):
                    currentSum += arr[k]  
                largestSum = max(currentSum,largestSum)
        return largestSum


a = A
print(a.printSubArraySum([-2,3,4,-1,5,-12,6,1,3]))

#Find out the largest sum of sub array suppose -2,3,4 = 5
# O(n) using Prefix sum algo- this is kadane's. O(1) space.


def printSubArraySum1(arr):
    currentSum = 0
    largestSum = 0
    for i in arr:
        currentSum = currentSum + i
        if currentSum < 0:
            currentSum = 0
        largestSum = max(currentSum,largestSum)

    print(largestSum)

printSubArraySum1([-2,3,4,-1,5,-12,6,1,3])


