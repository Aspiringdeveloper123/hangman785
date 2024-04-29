import random

# this file will contain the code for the first milestone
# create list of your 5 favourite fruits
word_list = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
print(word_list)

word = random.choice(word_list)
print(word)

#ask the user for input and check that the input is a single character
#also need to check that only alphabetical characters are provided by the user
#create conditional checks that must be passed before the input can be accepted

guess = input("Enter a single letter: ")
if (len(guess) == 1 and guess.isalpha() == True):
    print("Good guess!")
else:
    print("Oops! That is not a valid input")