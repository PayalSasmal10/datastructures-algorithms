"""
def main(): 
    print('main') 
    a = [1, 2, 3, 4] 
    b =    [5, 6, 7] 
    # c = [1, 8, 0, 1]

"""

a = [1, 2, 3, 4] 
b =    [5, 6, 7] 
sum = new_sum = 0
new_list = []
i = len(a)-1
while(i>=0):
    if i >=1:
        sum = a[i] + b[i-1] + int(new_sum)
    else:
        sum = a[i]
    if sum >= 10:
        str_sum = str(sum)
        new_sum = str_sum[0]
        new_list.append(int(str_sum[len(str_sum)-1]))
    else:
        new_list.append(sum)         
    i -= 1
print(new_list[::-1])
    




          

