# nearest largest to right
"""
i/p: [1, 3, 0, 0, 1, 2, 4]
o/p: [3, 4, 1, 1, 2, 4, -1]
"""
from inspect import stack


arr = [1, 3, 0, 0, 1, 2, 4]
class GreaterRight:
    new_list = []
    def nearestLargest(self, arr):
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                    self.new_list.append(arr[j])
                    break
            if len(arr)-1 == i:
                self.new_list.append(-1)

        return self.new_list


g = GreaterRight()
print(g.nearestLargest(arr))

print("................................................")
# OPtimize solution 
class GreaterRightOptimize:
    stack = []
    output = []
    def nearestLargest(self, arr):
        i = len(arr) - 1
        while(i>=0):
            if not self.stack:
                self.output.append(-1)
            elif self.stack[-1] > arr[i]:
                self.output.append(self.stack[-1])
            elif self.stack[-1] <= arr[i]:
                self.stack.pop()
                continue            
            self.stack.append(arr[i])
            i -= 1

        return self.output[::-1]



g = GreaterRightOptimize()
print(g.nearestLargest(arr))


