"""
def main(): 
    print('main') 
 TestCase1:
    a = [1, 2, 3, 4] 
    b =    [5, 6, 7] 
    # c = [1, 8, 0, 1]
TEst case2:
    a = [1, 2, 3, 4]     
    b = [5, 6, 7,9]
    #c =[6,9,1,3]

Test case3:
    a = [2, 3, 4]     
    b = [5, 6, 7,9]
    #c = [5,9,1,3]

"""

a = [2, 3, 4]     
b = [5, 6, 7, 9]
sum = new_sum = 0
new_list = []
i = max(len(a)-1, len(b) -1)
while(i>=0):
    if len(b) < len(a):
        if i >=1:
            sum = a[i] + b[i-1] + int(new_sum)
        else:
            sum = a[i]
    elif len(b) > len(a):
        if i>= 1:
            sum = a[i-1] + b[i] + int(new_sum)
        else:
            sum = b[i]
    elif len(a) == len(b):
        if i>= 1:
            sum = a[i] + b[i] + int(new_sum)
        else:
            sum = a[i] + b[i]
        
    if sum >= 10:
        str_sum = str(sum)
        new_sum = str_sum[0]
        new_list.append(int(str_sum[len(str_sum)-1]))
    else:
        new_list.append(sum)         
    i -= 1
print(new_list[::-1])
    




          

