# find the factorial of n number

class Factor:
    def fact(self,n):
        if n == 0:
            return 1
        return n * self.fact(n-1)


factobj = Factor
factobj.fact(5)
