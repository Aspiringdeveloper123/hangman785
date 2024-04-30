import random

# this file will contain the code for the first milestone
# create list of your 5 favourite fruits
list_of_favourite_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
print(list_of_favourite_fruits)

randomly_generated_fruit = random.choice(list_of_favourite_fruits)
print(randomly_generated_fruit)

guess_the_letter = input("Enter a single letter: ")

def validate_input(user_input):
    return len(guess_the_letter) == 1 and guess_the_letter.isalpha()

if validate_input(guess_the_letter):
    print("Good guess!")

else: 
    print(" Oops! That is not a valid input")



