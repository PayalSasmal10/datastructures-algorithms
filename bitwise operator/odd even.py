# if the last bit of the number is 0 then even else 1
class oddEven:
    def oddandeven(x):
        if x&1:
            return "Odd"
        else:
            return "Even"


oddeven = oddEven
print(oddeven.oddandeven(6)
)