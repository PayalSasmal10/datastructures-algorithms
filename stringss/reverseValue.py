
# time complexity O(nlogn)
namereverse = "payal2 am1 i0 sasmal3"

sortedValue = sorted(namereverse, key=len)
sortedValue = "".join(sortedValue)

removeList = "".join([i for i in sortedValue if not i.isdigit()])
print(removeList)


