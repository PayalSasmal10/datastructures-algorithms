# Tower of Hanoi

from select import select
from shutil import move

class Hanoi:
    def hanoi(self,s, d, h, n):
        if n == 1:
            self.moveHanoi(s,d,h,n)
            return
        # moving plates from source to helping tower
        self.hanoi(s, h, d, n-1)
        self.moveHanoi(s,d,h,n)
        # moving plates from helping to destination tower
        self.hanoi(h,d,s,n-1)
    
    def moveHanoi(self,s,d,h,n):
        print(f"move plate {n} from {s} to {d} using {h}")


h = Hanoi()
h.hanoi('A', 'C', 'B', 3)