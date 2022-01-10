# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(words):
        test = []
        newreverse = ''
        for i in words:
            newreverse = ''
            for j in i:
                newreverse = j + newreverse
                if i == newreverse:
                   test.append(i)
        return test[0]
                
                
s = Solution
s.firstPalindrome(["abc","car","ada","racecar","cool"])