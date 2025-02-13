from collections import Counter

sample_dict = {
    'apple': 'A sweet red or green fruit',
    'banana': 'A long yellow fruit',
    'carrot': 'An orange root vegetable',
    'dog': 'A domesticated carnivorous mammal',
    'elephant': 'A large herbivorous mammal with a trunk',
    'frog': 'A small amphibian with long hind legs',
    'guitar': 'A small amphibian with long hind legs',
    'house': 'A building for human habitation',
    'island': 'A piece of land surrounded by water',
    'jacket': 'A garment for the upper body'
}

programming_languages = {
    'Python': 'Guido van Rossum',
    'Java': 'James Gosling',
    'C': 'Dennis Ritchie',
    'C++': 'Bjarne Stroustrup',
    'JavaScript': 'Brendan Eich',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'Swift': 'Chris Lattner',
    'Go': 'Robert Griesemer, Rob Pike, and Ken Thompson',
    'Kotlin': 'JetBrains'
}

#Problem 1

key = "apple"
try:
    print(sample_dict[key])
except:
    print("There is no such key.")

#Problem 2 

key = "apple"
keys, values = zip(*sample_dict.items())
if key in keys:
    print(True)
else:
    print(False)

#Problem 3

keys, values = zip(*sample_dict.items())
print(len(keys))

#Problem 4

keys, values = zip(*sample_dict.items())
print(keys)

#Problem 5

keys, values = zip(*sample_dict.items())
print(values)

#Problem 6

result = {**programming_languages,**sample_dict}
print(result)

# Problem 7

key = "apple"
keys,values = zip(*programming_languages.items())
try:
    if key in keys:
        programming_languages.pop(key)
        print(programming_languages)
except:
    print("There is no such key.")

# Problem 8

dictionary = {}

# Problem 9

if programming_languages:
    print(True)
else:
    print(False)

# Problem 10 

key = "Python"
print(f"{key}:{programming_languages[key]}")

# Problem 11

key = "Python"
programming_languages[key]="Komronbek"

# Problem 12

value = 'A small amphibian with long hind legs'
result = list(sample_dict.values()).count(value)
print(result)

# Print 13

keys,values = zip(*programming_languages.items())
new = dict(zip(values,keys))
print(new)

# Problem 14

key_list = []
value = 'A small amphibian with long hind legs'
for values, keys in sample_dict.items():
    if keys == value:
        key_list.append(values)
print(key_list)

# Problem 15

keys,values = zip(*programming_languages.items())
new = dict(zip(values,keys))
print(new)

# Problem 16

for value in programming_languages.values():
    if type(value)==dict:
        print(True)
    else:
        print(False)

# Problem 17

for value in programming_languages.values():
    if type(value)==dict:
        print(value.items())
    else:
        print(False)

# Problem 18

my_dict = {'name': 'Bob'}
email = my_dict.setdefault('email', 'Not Provided')
print(email)

# Problem 19

keys,values = zip(*programming_languages.items())
values = set(values)
for val in values:
    print(val)

# Problem 20

my_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)

# Problem 21

my_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[0]))
print(sorted_by_values)

# Problem 22

my_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
for key,value in my_dict.items():
    if "a" in key:
        print(my_dict[key])
    else:
        continue

# Problem 23

for i in programming_languages.keys():
    for j in sample_dict.keys():
        if i==j:
            print(True)
        else:
            print(False)

# Problem 24

tuple_pairs = (('a', 1), ('b', 2), ('c', 3))
result_dict = dict(tuple_pairs)
print(result_dict)

#Problem 25

for key,value in programming_languages.items():
    print(f"{key}:{value}")
    break