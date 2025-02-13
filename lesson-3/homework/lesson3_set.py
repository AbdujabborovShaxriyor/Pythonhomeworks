# Problem 1 

set1 = {1,2,3,3}
set2 = {4,5,6,6}
new_set = set(set1.union(set2))
print(new_set)

# Problem 2

set1 = {1,2,3,3,4}
set2 = {4,5,6,6}
new_set = set(set1.intersection(set2))
print(new_set)

# Problem 3

set1 = {1,2,3,3,4}
set2 = {4,5,6,6}
new_set = set(set1.difference(set2))
print(new_set)

# Problem 4

set1 = {1,2,3,3,4}
set2 = {4,5,6,6}

if set1 in set2:
    print(True)
else:
    print(False)

# Problem 5

set1 = {1,2,3,3,4}
element = 0
if element in set1:
    print(True)
else:
    print(False)

# Problem 6

set1 = {1,2,3,3,4}
print(len(set1))

# Problem 7

lists = [1,1,2,2,3,3,3,3,4]
unique = set(lists)
print(unique)

# Problem 8

elements = {1,2,3,4,4,5,4,3,6}
element = 3
elements.remove(element)
print(elements)

# Problem 9

elements = {1,2,3,4,4,5,4,3,6}
elements.clear()

# Problem 10

elements = {1,2,3,4,4,5,4,3,6}
if elements:
    print(True)
else:
    print(False)

# Problem 11

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.symmetric_difference(set2))

# Problem 12

elements = {1,2,3,4,4,5,4,3,6}
element = 7
if element not in elements:
    elements.add(element)
print(elements)

# Problem 13

elements = {1,2,3,4,4,5,4,3,6}
elements.pop()
print(elements)

# Problem 14

elements = {1,2,3,4,4,5,4,3,6}
print(max(elements))

# Problem 15

elements = {1,2,3,4,4,5,4,3,6}
print(min(elements))

# Problem 16

elements = {1,2,3,4,4,5,4,3,6}
elements = list(elements)
for element in elements:
    if element%2!=0:
        elements.remove(element)
elements = set(elements)

# Problem 17

elements = {1,2,3,4,4,5,4,3,6}
elements = list(elements)
for element in elements:
    if element%2==0:
        elements.remove(element)
elements = set(elements)

# Problem 18

element = set()
for i in range(0,10):
    element.add(i)
print(element)

# Problem 19

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))

#Problem 20

set1 = {1,2,3}
set2 = {3,4,5}
checker = 0
for i in set1:
    for j in set2:
        if i==j:
            checker+=1
if checker==0:
    print(True)
else:
    print(False)

#Problem 21

elements = [1,2,3,4,4,5,4,3,6]
elements = set(elements)
elements = list(elements) 
print(elements)

#Problem 22

elements = [1,2,3,4,4,5,4,3,6]
elements = set(elements)
print(len(elements))      

#Problem 23

element = set()
for i in range(0,10):
    element.add(i)
print(element)