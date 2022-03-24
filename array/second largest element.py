class A:
    # 1st way o(nlogn)
    def arrSecondLargest(self, arr):
        arr.sort()
        return arr[-2]
    
    # o(n) time complexity
    def arrsecondLargest1(self,arr):
        first_ele = arr[0]
        second_ele = arr[1]
        for i in arr:
            if i > first_ele:
                second_ele = first_ele
                first_ele = i
            elif i> second_ele and i != first_ele:
                second_ele = i
        return second_ele
            


arr = [12, 35, 1, 10, 38, 1]
a = A()
print(a.arrSecondLargest(arr))
print(a.arrsecondLargest1(arr))