# time complexity is O(n) 
palindromString = input()

def palindrome(palimdromString):
    reversePalindrom = ''
    for i in palimdromString:
        reversePalindrom = i + reversePalindrom

    if reversePalindrom == palimdromString:
        print("It's a palindrome string")
    else:
        print("It's not a string")


palindrome(palindromString)

