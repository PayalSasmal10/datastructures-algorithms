# time complexity is O(n) 
palindromString = input()

def palindrome(palimdromString):
    reversePalindrom = ''
    for i in palimdromString:
        reversePalindrom = i + reversePalindrom

    if reversePalindrom == palimdromString:
        print("It's a palindrome string 1")
    else:
        print("It's not a palindrom string 1")


palindrome(palindromString)

def palindrome1(palindromString):
    if palindromString == reversed(palindromString):
        print("It's a palindrom string 2")
    else:
        print("It's not a palindrom string 2")

palindrome1(palindromString)