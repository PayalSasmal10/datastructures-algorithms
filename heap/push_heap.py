import heapq
class Heap:

    def __init__(self, arr) -> None:
        self.arr = arr

    def push_at_back(self, data):
            heapq.heapify(self.arr)
            heapq.heappush(self.arr,data)
            return list(self.arr)

    def get_min_heap(self):
        heapq.heapify(self.arr)
        return self.arr[0]
    
    def get_max_heap(self):
        return self.arr[len(self.arr)-1]

    
   


h = Heap([5, 7, 9, 1, 3])
print(h.push_at_back(4))
print(h.get_min_heap())
print(h.get_max_heap())