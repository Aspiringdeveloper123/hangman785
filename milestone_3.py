import random

list_of_favourite_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
print(list_of_favourite_fruits)

randomly_generated_fruit = random.choice(list_of_favourite_fruits)
print(randomly_generated_fruit)

while True:  # let the code run continuosly 
    guess_the_letter = input("Enter a single letter: ")

    if len(guess_the_letter) == 1 and guess_the_letter.isalpha():
        break

    else:   
        print("Invalid letter. Please, enter a single alphabetical character")

print("Good guess")