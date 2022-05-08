# nearest largest to right
"""
i/p: [1, 3, 0, 0, 1, 2, 4]
o/p: [3, 4, 1, 1, 2, 4, -1]
"""
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
