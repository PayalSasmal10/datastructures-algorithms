# Given two strings A and B. Check if one string is permutation of the other. A 
# permutation of a string is another that contains same character.
# Ex- abcd and dabc are permutation.

string_permutation1 = input()
string_permutation2 = input()

def permutation(string_permutation1,string_permutation2):
    string_permutation_1 = sorted(string_permutation1)
    string_permutation_2 = sorted(string_permutation2)
    if string_permutation_1 == string_permutation_2:
        return "Yes"
    else:
        return "No"

print(permutation(string_permutation1,string_permutation2))
