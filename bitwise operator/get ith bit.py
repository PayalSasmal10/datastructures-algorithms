# Find the ith bit

class ithBit:
    def findithbit(n,i):
        mask = 1<<i
        return 1 if n & mask else 0


ithbitfind = ithBit
print(ithbitfind.findithbit(5,2))