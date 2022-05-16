# print unique subset 
"""
i/p: "aab"
o/p: "", a, aa, ab, aab, b
"""

class A:
    new_dict = {}
    def unique_subset(self, sub_str):
        output = ""
        self.solve(sub_str,output)

    def solve(self,sub_str,output):
        if len(sub_str) == 0:
            self.new_dict[output] = 1
            self.get_dict(self.new_dict)
            return
        

        output1 = output
        output2 = output
        output2 += sub_str[0]
        sub_str = sub_str[1:]
        self.solve(sub_str,output1)
        self.solve(sub_str,output2)

        


    def get_dict(self,dictt):
        for i in dictt:
            print(i)

        



a = A()
sub_str = "aab"
a.unique_subset(sub_str)
