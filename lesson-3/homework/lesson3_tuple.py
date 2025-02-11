#Problem 1

elements = ("hello",4,5,6,"my",4,4)
print(elements.count(4))

#Problem 2

elements = (1,2,3,4,5,6,44,2)
print(max(elements))

#Problem 3

elements = (1,2,3,4,5,6,44,2)
print(min(elements))

#Problem 4

elements = (1,2,3,4,5,6,44,2)
element = 0
print(element in elements)

#Problem 5

elements = (1,2,3,4,5,6,44,2)
if elements:
    print(elements[0])
else:
    print("The tuple is empty")

#Problem 6

elements = (1,2,3,4,5,6,44,2)
if elements:
    print(elements[-1])
else:
    print("The tuple is empty")

#Problem 7

elements = (1,2,3,4,5,6,44,2)
print(len(elements))

#Problem 8

elements = (1,2,3,4,5,6,44,2)
new_elements = elements[0:3]
print(new_elements)

#Problem 9

elements = (1,2,3,4,5,6,44,2)
new_elements = elements[0:3]
newest = elements + new_elements
print(newest)

#Problem 10

elements = (1,2,3,4,5,6,44,2)
if elements:
    print(True)
else:
    print(False)

#Problem 11

elements = (1,2,3,4,5,6,44,2)
element = 2
for i in range(0,len(elements)):
    if elements[i]==element:
        print(i)

#Problem 12

elements = (1,2,3,4,5,6,44,2)
new_elements = tuple(sorted(elements))
print(new_elements[-2])

#Problem 13

elements = (1,2,3,4,5,6,44,2)
new_elements = tuple(sorted(elements,reverse=True))
print(new_elements[-2])

#Problem 14

element = (1,)

#Problem 15

numbers = [1,2,3,4,4,5]
new_numbers = tuple(numbers)
print(new_numbers)

#Problem 16

checker = 0
elements = (1,2,3,4,5,6,6,44,2)
for i in range (0,len(elements)):
    if i==len(elements)-1:
        break
    else:
        if elements[i]>elements[i+1]:
            checker+=1
if checker==0:
    print(True)
else:
    print(False)

#Problem 17

elements = (1,2,3,4,5,6,6,44,2)
subtuple = elements[0:7]
print(max(subtuple))

#Problem 18

elements = (1,2,3,4,5,6,6,44,2)
subtuple = elements[0:7]
print(min(subtuple))

#Problem 19

elements = (1,2,3,4,5,6,6,44,2)
element = 2
new_tuple = list(elements)
for i in range(0,len(new_tuple)):
    if new_tuple[i]==element:
        new_tuple.remove(new_tuple[i])
        break
new_tuple = tuple(new_tuple)
print(new_tuple)

#Problem 20

elements = (1,2,3,4,5,6,6,44,2)
element1 = elements[:3]
element2 = elements[3:6]
element3 = elements[6:]
new_elements = (element1,element2,element3)
print(new_elements)

#Problem 21

elements = (1,2,3,4,5,6,6,44,2)
element = 3
new_elements = []
for i in range(0,len(elements)):
    for j in range(0,element):
        new_elements.append(elements[i])
new_elements = tuple(new_elements)
print(new_elements)

#Problem 22

elements = []
for i in range(0,10):
    elements.append(i)
elements = tuple(elements)
print(elements)

#Problem 23

elements = (1,2,3,4,5,6,6,44,2)
elements = list(elements)
elements.sort(reverse=True)
elements = tuple(elements)
print(elements)

#Problem 24

elements = (1,2,3,4,5,6,6,44,2)
if elements==elements[::-1]:
    print(True)
else:
    print(False)

#Problem 25

numbers = (1, 2, 3, 2, 1)
only_unique= []

for num in numbers:
    if num not in only_unique:
        only_unique.append(num)
only_unique = tuple(only_unique)
print(only_unique)
