# Guess the secret number (Computer)
import random

# def guess(number):
#   random_number = random.randint(0,number)
#   print(random_number)
#   guess = 0
#   while guess != random_number:
#     guess = int(input(f'Guess number bewteen 1 and {number}'))
#     if guess < random_number:
#       print("Sorry This is low number")
#     elif guess > random_number:
#       print("This is higher number ")
#   print("Congratulations You have entered a correct number")

# guess(10)


list = [1,2,3,4,5,6,7]
list2 = [4,5,6,7,8,9]

list.append(list2)
print(list)