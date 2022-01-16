# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(nums1, nums2):
        insertion_list = []
        # insertion_list = [i for i in nums1 if i in nums2 and (j+1)>=len(nums2)]
        for i in set(nums1):
            if i in nums2:
                n = min(nums1.count(i), nums2.count(i))
                insertion_list += [i for j in range(n)]
                print(insertion_list)
        return insertion_list

s = Solution
print(s.intersect([4,9,5],[9,4,9,8,4,5]))