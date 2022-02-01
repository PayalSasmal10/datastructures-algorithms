
# time complexity O(nlogn)
from cgi import test


namereverse = "payal2 am1 i0 sasmal3"

# sortedValue = sorted(namereverse, key=len)
# sortedValue = "".join(sortedValue)

# removeList = "".join([i for i in sortedValue if not i.isdigit()])
# print(removeList)


class Solution:
    def sortSentence(s: str) -> str:
        test = s.split(" ")
        i = j = 0
        test1 = ""
        while i<=len(test)-1:
            #print(test[i][-1])
            if test[i][-1] == j:
                print(test[i])
                j += 1
            i += 1
            
                         
st = Solution
st.sortSentence(namereverse)          
            

