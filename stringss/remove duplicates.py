# remove duplicates from a string and return the string in sorted order
# input=geeksforgeeks, o/p=efgkors

string_input = input()

def remove_duplicates(string_input):
    convert_set = set(string_input)
    test = sorted(convert_set)
    new_string = ''
    for i in test:
        new_string += i

    return new_string


print(remove_duplicates(string_input))