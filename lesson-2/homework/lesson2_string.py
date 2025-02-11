#Problem 1

name = input("Enter your name: \n>>>")
age = int(input("Enter your age: \n>>>"))
print(name)
print(age)

#Problem 2

txt = 'LMaasleitbtui'
car_names = ["Malibu","Lasetti","Cobolt","Damas"]

for car in car_names:
    if car.lower() in txt.lower():
        print(car)

#Problem 3

string  = input("Enter the word: \n>>>")
print(len(string))
print(string.lower())
print(string.upper())

# Problem 4

is_palindrome = input("Enter the word: \n>>>")
checker = True
for i in range(0,len(is_palindrome)//2):
    if is_palindrome[i]==is_palindrome[-i]:
        continue
    else:
        checker=False
if checker:
    print(f"{is_palindrome} is a palindrome")
else:
    print(f"{is_palindrome} is not a palindrome")

# Problem 5

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 
    'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
]

vowel_counter = 0
consonant_counter = 0

word =  input("Enter the word: \n>>>")
for i in range(0,len(word)):
    if word[i].lower() in vowels:
        vowel_counter+=1
    elif word[i].lower() in consonants:
        consonant_counter+=1
print(f"The word {word} has {vowel_counter} vowels and {consonant_counter} consonants")

# Problem 6

str1 = input("Enter the first string: \n>>>")
str2 = input("Enter the second string: \n>>>")
if str1 in str2 or str2 in str1:
    print(True)
else:
    print(False)

#Problem 7

sentence = input("Input sentence: ")
replace = input("Replace: ")
replace_with = input("With: ")
new_sentence = sentence.split(replace)
print(new_sentence[0]+replace_with)

# Problem 8

string  = input("Enter the word: ")
print(string[0],string[-1])

#Problem 9

string  = input("Enter the word: ")
for i in range (1,len(string)+1):
    print(string[-i],end="")

# Problem 10

sentence = input("Input sentence: ")
new_sentance = sentence.split(" ")
print(len(new_sentance))

#Problem 11

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
checker=0
word = input("Enter the word: ")
for digit in digits:
    if digit in word:
        print(f"The word {word} has {digit} digit")
        checker+=1
        break
if checker==0:
    print(f"The word {word} has not got any digits")

#Problem 12

words = []
quantity = int(input("Enter the number of words you wanna enter: "))
for i in range(0,quantity):
    word = input("Enter the word: ")
    words.append(word)
result = "-".join(words)
print(result)

#Problem 13

string = input("Enter the string: ")
new_string = string.replace(" ","")
print(new_string)

#Problem 14

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string1==string2:
    print(True)
else:
    print(False)

#Problem 15

sentence = input("Enter the sentence: ")
new_sentence = sentence.split(" ")
for word in new_sentence:
    print(word[0],end="")

#Problem 16

string = input("Enter the string: ")
letter = input("Enter one letter from your string: ")
new_string = string.replace(letter,"")
print(new_string)

#Problem 17

vowel = ["a",'e','i','o','u']
word = input("Enter the word: ")
for letter in word:
    if letter in vowel:
        word=word.replace(letter,"*")
print(word)

# Problem 18

sentence = input("Enter the sentence: ")
new_sentence = sentence.split(" ")
print(f"The sentence starts with {new_sentence[0]}")
print(f"The sentence ends with {new_sentence[-1]}")