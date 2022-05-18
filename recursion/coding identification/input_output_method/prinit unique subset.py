# print unique subset 
"""
i/p: "aab"
o/p: "", a, aa, ab, aab, b
"""

class A:
    
    def unique_subset(self, sub_str):
        output = ""
        self.solve(sub_str,output)

    def solve(self,sub_str,output, new_dict = {}):
        if len(sub_str) == 0:
            new_dict[output] = 1

            return
        

        output1 = output
        output2 = output
        output2 += sub_str[0]
        sub_str = sub_str[1:]
        self.solve(sub_str,output1)
        self.solve(sub_str,output2)

        

        



a = A()
sub_str = "aab"
a.unique_subset(sub_str)
