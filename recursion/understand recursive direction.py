# print number 1...N recursively in increasing order and decreasing order

#increasing order
def recursiveDirectionIncreasingOrder(n):
    if n == 0:
        return n
    else:
        recursiveDirectionIncreasingOrder(n-1)
        print(n)


recursiveDirectionIncreasingOrder(10)

print("##############################################################")
#deacreasing order

def recursiveDirectionDecreasingOrder(n):
    if n == 0:
        return n
    else:
        print(n)
        return recursiveDirectionDecreasingOrder(n-1)

recursiveDirectionDecreasingOrder(10)