# Find out all permutation

strr = "ABC"
print(strr[2:])
# output: ABC, ACB, BCA, BAC, CAB, CBA
class A:
    def permutation(self, strr):
        output = ""
        self.solve(strr,output)

    def solve(self, strr, output):
        if len(strr) == 0:
            print(output)
            return
        for i in range(len(strr)):
            single_ch = strr[i]
            output1 = strr[0:i]
            output2 = strr[i+1:]
            remaining_str = output1 + output2
            self.solve(remaining_str, single_ch+output)

a = A()
a.permutation(strr)
