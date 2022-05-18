# find palindrome using recursion

strr = "aabcaa"

class A:
    def isPalindrom(self, strr, i, j):
        
        if i >= j:
            return True
        
        if strr[i] != strr[j]:
            return False
        
        return self.isPalindrom(strr, i+1, j-1)


a = A()
print(a.isPalindrom(strr, 0, len(strr)-1))


        


