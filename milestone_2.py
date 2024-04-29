import random

# this file will contain the code for the first milestone
# create list of your 5 favourite fruits
list_of_favourite_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
print(list_of_favourite_fruits)

randomly_generated_fruit = random.choice(list_of_favourite_fruits)
print(randomly_generated_fruit)

#ask the user for input and check that the input is a single character
#also need to check that only alphabetical characters are provided by the user
#create conditional checks that must be passed before the input can be accepted

guess_the_letter = input("Enter a single letter: ")
if (len(guess_the_letter) == 1 and guess_the_letter.isalpha() == True):
    print("Good guess!")
else:
    print("Oops! That is not a valid input")