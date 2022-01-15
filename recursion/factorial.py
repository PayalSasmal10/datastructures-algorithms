# find the factorial of n number

# class Factor:
#     def fact(self,n):
#         if n == 0:
#             return 1
#         return n * self.fact(n-1)


# factobj = Factor
# factobj.fact(5)

class Solution:
    def merge(nums1, m: int, nums2) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        test = []
        for i in range(m-1):
            test.append(nums1[i])
        test2 = test+nums2
        test2.sort()
        return test2
                


tets = Solution
print(tets.merge([0],1,[1]))
