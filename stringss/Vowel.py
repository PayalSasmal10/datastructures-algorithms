# find the vowel from the string

string_input = input()

def vowelfind(string_input):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    new_vowels = ""
    for i in string_input:
        if i in vowels:
            new_vowels += i

    return new_vowels


print(vowelfind(string_input))