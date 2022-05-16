subset_str = "abc"
class A:

    def subset_recursive(self,subset_str):
        output = ""
        self.solve(subset_str,output)

    
    def solve(self,inpute, output):
        if len(inpute) == 0:
            print(output)
            return
        output1 = output
        output2 = output
        output2 += inpute[0]
        # remove first position value from inpute string
        inpute = inpute[1:]
        # this is for output1
        self.solve(inpute,output1) 
        # this is for output2
        self.solve(inpute,output2)

        



a = A()

print("recursive way")
a.subset_recursive(subset_str)