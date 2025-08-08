'''DAY 3'''

'''1. Write a function to check whether a given string is a pangram (contains all letters of the'''

def panagram(sentence):
    sentence = sentence.lower()
    letters = set()

    for char in sentence:
        if 'a' <= char <= 'z':
            letters.add(char)
        
    return len(letters) == 26

text = input("Enter a sentence: ")

if(panagram(text)):
    print("The sentence is a paragram")
else:
    print("The sentence is not a panagram")

'''2. Write a function that takes a sentence and returns the word with the maximum length'''

def long_word(sentence):
    words = sentence.split()
    max_word = ""

    for word in words:
        if(len(word) > len(max_word)):
            max_word = word

    return max_word

text = input("Enter a sentence: ")

result = long_word(text)

print(f"The Word with maximum length is: {result}")

'''3. Write a function to count the number of uppercase and lowercase characters in a string.'''

def count_case(text):
    upper_case = 0
    lower_case = 0

    for char in text:
        if('A' <= char <= 'Z'):
            upper_case += 1
        elif('a' <= char <= 'z'):
            lower_case += 1
    return upper_case, lower_case

text = input("Enter a sentence with a few capital terms: ")

uppercase, lowercase = count_case(text)

print(f"The number of Upper Case Characters are: {uppercase}")
print(f"The number of Lower Case Characters are: {lowercase}")

'''----------------------------------------------------------------------------------------------------------'''