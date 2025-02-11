#Problem 1

cars = ["ford","bmw","mercedes","bmw"]
print(cars.count("bmw"))

#Problem 2

numbers = [1,2,3,4,4,5]
sum = 0
for i in range(0,len(numbers)):
    sum+=numbers[i]
print(f"The sum is: {sum}")

#Problem 3

numbers = [1,2,3,4,4,5]
largest = numbers[0]
for num in numbers:
    if largest<num:
        largest=num
print(largest)

#Problem 4

numbers = [1,2,3,4,4,5]
largest = numbers[0]
for num in numbers:
    if largest>num:
        largest=num
print(largest)

#Problem 5

numbers = [1,2,3,4,4,5]
number = 0
if number in numbers:
    print(True)
else:
    print(False)

#Problem 6

numbers = [1,2,3,4,4,5]

if len(numbers)==0:
    print("The list is empty")
else:
    print(numbers[0])

#Problem 7

numbers = [1,2,3,4,4,5]

if len(numbers)==0:
    print("The list is empty")
else:
    print(numbers[-1])

#Problem 8

numbers = [1,2,3,4,4,5]
new_numbers = numbers[:3]
print(new_numbers)

#Problem 9

numbers = [1,2,3,4,4,5]
new_numbers = numbers[::-1]
print(new_numbers)

#Problem 10

numbers = [10,2,3,4,4,5]
new_numbers = sorted(numbers)
print(new_numbers)

#Problem 11

numbers = [1,10,2,3,1,4,4,5,7]
new_numbers = []
for i in range(0,len(numbers)):
    if numbers[i] not in new_numbers:
        new_numbers.append(numbers[i])
print(new_numbers)        

#Problem 12

numbers = [1,10,2,3,1,4,4,5,7]
number = 100
numbers.insert(0,number)
print(numbers)


#Problem 13

numbers = [1,10,2,3,1,4,4,5,7]
number = 10
index = numbers.index(number)
print(index)

#Problem 14

numbers = [1,2,3,4,4,5]

if len(numbers)==0:
    print(False)
else:
    print(True)

#Problem 15

numbers = [1,2,3,4,4,5]
counter=0
for num in numbers:
    if num%2==0:
        counter+=1
print(f"The number of even numbers is: {counter}")

#Problem 16

numbers = [1,2,3,4,4,5]
counter=0
for num in numbers:
    if num%2!=0:
        counter+=1
print(f"The number of even numbers is: {counter}")

#Problem 17

list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1+list2
print(list3)

#Problem 18

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6]

if any(list1[i:i + len(list2)] == list2 for i in range(len(list1) - len(list2) + 1)):
    print(True)
else:
    print(False)

#Problem 19

numbers = [1,10,2,3,1,4,4,5,7]
number = 10
index = numbers.index(number)
numbers[index]=100
print(numbers)

#Problem 20

numbers = [1,10,2,3,1,4,4,5,7]
new_list = sorted(numbers,reverse=True)
print(new_list[1])

#Problem 21

numbers = [1,10,2,3,1,4,4,5,7]
new_list = sorted(numbers)
print(new_list[1])

#Problem 22

numbers = [1,10,2,3,1,4,4,5,7]
new_numbers = []
for i in range(0,len(numbers)):
    if numbers[i]%2==0:
        new_numbers.append(numbers[i])
print(new_numbers)

#Problem 23

numbers = [1,10,2,3,1,4,4,5,7]
new_numbers = []
for i in range(0,len(numbers)):
    if numbers[i]%2!=0:
        new_numbers.append(numbers[i])
print(new_numbers)

#Problem 24

length = len(numbers = [1,10,2,3,1,4,4,5,7])

#Problem 25

numbers = [1,10,2,3,1,4,4,5,7]
numbers_copy = numbers.copy()

#Problem 26

numbers = [1,10,2,3,1,4,4,5,7,7]
if len(numbers)%2==0:
    print(numbers[len(numbers)//2-1],numbers[len(numbers)//2])
else:
    print(numbers[len(numbers)//2])

#Problem 27

numbers = [1, 9, 3, 7, 5, 2, 8]
start_index = 1
end_index = 4
max_element = numbers[start_index:end_index]
print(max(max_element))

#Problem 28 

numbers = [1, 9, 3, 7, 5, 2, 8]
start_index = 1
end_index = 4
max_element = numbers[start_index:end_index]
print(min(max_element))

#Problem 29

numbers = [1, 9, 3, 7, 5, 2, 8]
index = 5
numbers.remove(numbers[5])
print(numbers)

#Problem 30

numbers = [1, 9, 3, 7, 5, 2, 8]
checker = 0
numbers.sort()
for i in range(0,len(numbers)-1):
    if i==len(numbers):
        break
    else:
        if numbers[i]<numbers[i+1]:
            continue
        else:
            checker+=1
if checker==0:
    print(True)
else:
    print(False)

#Problem 31

numbers = [1, 9, 3, 7, 5, 2, 8]
number = int(input("Enter the how many times should the number repeated: "))
new_numbers = [numbers[i] for i in range(0,len(numbers)) for j in range(0,number)]
print(new_numbers)

#Problem 32

numbers = [1, 9, 3, 7, 5, 2, 8]
other_numbers = [2,3,5,6,7]
numbers.extend(other_numbers)
print(numbers)

#Problem 33

numbers = [1, 9, 3, 7, 1, 5, 2, 8, 1]
number = 1
for i in range(0,len(numbers)):
    if numbers[i]==number:
        print(i)

#Problem 34

numbers = [1, 9, 3, 7, 5, 2, 8]
new_numbers = [0]*len(numbers)
for i in range(0,len(numbers)):
    if i==len(numbers)-1:
        new_numbers[0]=numbers[len(numbers)-1]
    else:
        new_numbers[i+1]=numbers[i]
print(new_numbers)

#Problem 35

numbers = []
for i in range(0,10):
    numbers.append(i)

#Problem 36

numbers = [1, 9, 3, 7, 5, 2, 8,-1,2,-4,-3,-10]
sum = 0
for num in numbers:
    if num>0:
        sum+=num
print(sum)
    
#Problem 37

numbers = [1, 9, 3, 7, 5, 2, 8,-1,2,-4,-3,-10]
sum = 0
for num in numbers:
    if num<0:
        sum+=num
print(sum)

#Problem 38

checker = 0
numbers = [1, 2, 3, 2, 1]

for i in range(len(numbers) // 2):
    if numbers[i] != numbers[-(i + 1)]:
        checker += 1

if checker == 0:
    print(True)
else:
    print(False)

#Problem 39

parent_list = []
sub_list1 = []
sub_list2 = []
sub_list3 = []

sub_list1_len = int(input("Enter the length of the first sub list: "))
for i in range(0,sub_list1_len):
    sub1_element = input(f"Enter an element {i+1} to a first sub list: ")
    sub_list1.append(sub1_element)

sub_list2_len = int(input("Enter the length of the second sub list: "))
for i in range(0,sub_list2_len):
    sub2_element = input(f"Enter an element {i+1} to a second sub list: ")
    sub_list2.append(sub2_element)
    
sub_list3_len = int(input("Enter the length of the third sub list: "))
for i in range(0,sub_list3_len):
    sub3_element = input(f"Enter an element {i+1} to a third sub list: ")
    sub_list3.append(sub3_element)
    
parent = [sub_list1,sub_list2,sub_list3]
print(parent)

#Problem 40

numbers = [1, 2, 3, 2, 1]
only_unique= []
for num in numbers:
    if num not in only_unique:
        only_unique.append(num)
print(only_unique)
