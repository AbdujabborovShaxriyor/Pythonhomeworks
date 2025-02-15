import random as r

#Problem 1

list1 = [1,2,3,4]
list2 = [3,4,5,6]
uncommon=[]
for item in list1:
    if item not in list2:
        uncommon.append(item)
for item in list2:
    if item not in list1:
        uncommon.append(item)
print(uncommon)

#Problem 2

limit = int(input("Enter the limit: "))
for i in range(1,limit):
    print(i*i)

#Problem 3

vowels = ["a",'e',"i","o",'u']
txt = input("Enter the text: ")
counter = 1
for letter in txt:
    if counter%3==0:
        if letter in vowels or letter=="_" or letter==len(txt)-1:
            print(txt[counter-1],end="")
            print(txt[counter],end="")
            print("_",end="")
        else:
            print(txt[counter-1],end="")
            print("_",end="")
        counter+=1
    else:
        print(txt[counter-1],end="")
        counter+=1

#Problem 4

number = r.randint(0,100)
counter = 1
while True:
    guess = int(input("Enter your guess: "))
    if guess==number:
        print(f"Congratualtions you won in {counter} attempts!!!")
        answer = input("If you wanna try again enter Yes/yes/Y/ok\n>>>")
        if answer.lower() == "y" or answer.lower() == "yes" or answer.lower() == "ok":
            number = r.randint(0,100)
            counter=1
            continue
        else:
            break
    else:
        if counter<=10:
            counter+=1
            if guess>number:
                print("High")
            elif guess<number:
                print("Low")
        else:
            print(f"Your attempts has exceeded 10 so you lose! The number was {number}")
            break

#Problem 5

import string
capital_letters = list(string.ascii_uppercase)
checker = 0
password = input("Create a password: ")
if len(password)<8:
    print("Password is too short. Reenter the password")
for i in capital_letters:
    if i in password:
        checker=1
if checker==0:
    print("The password must contain at least 1 capital letter")
elif checker!=0 and len(password)>=8:
    print("Strong password")

#Problem 6

print(2)
for num in range(3,100):
    checker = 0
    for specific_num in range(2,num//2+1):
        if num%specific_num==0:
            checker+=1
    if checker==0:
        print(num)        

#Bonus challenge

rock = 'r'
paper = 'p'
scissors = 's'
choices = [rock,paper,scissors]
human_point = 0
computer_point = 0
while True:
    computer_choice = r.choice(choices)
    human_choice = input("Enter your choice(s-scissors,r-rock,paper-p): ")  
    if human_point<5 and computer_point<5:
        if computer_choice==human_choice:
            print(f"Both sides have chosen {human_choice}")     
            continue
        elif computer_choice=='r' and human_choice=='p':
            print("Computer chose rock and human chose paper.Human won!!!")
            human_point+=1
            print(f"Human---{human_point} : Computer---{computer_point}")
        elif computer_choice=='r' and human_choice=='s':
            print("Computer chose rock and human chose scissors.Computer won!!!")
            computer_point+=1
            print(f"Human---{human_point} : Computer---{computer_point}")
        elif computer_choice=='p' and human_choice=='s':
            print("Computer chose paper and human chose scissors.Human won!!!")
            human_point+=1
            print(f"Human---{human_point} : Computer---{computer_point}")
        elif computer_choice=='p' and human_choice=='r':
            print("Computer chose paper and human chose rock.Computer won!!!")
            computer_point+=1
            print(f"Human---{human_point} : Computer---{computer_point}")
        elif computer_choice=='s' and human_choice=='r':
            print("Computer chose scissors and human chose rock.Human won!!!")
            human_point+=1
            print(f"Human---{human_point} : Computer---{computer_point}")
        elif computer_choice=='s' and human_choice=='p':
            print("Computer chose scissors and human chose paper.Computer won!!!")  
            computer_point+=1   
            print(f"Human---{human_point} : Computer---{computer_point}")  
    elif human_point==5 and computer_point<5:
        print("Human won!!!")
    elif computer_point==5 and human_point<5:
        print("Computer won!!!")
        