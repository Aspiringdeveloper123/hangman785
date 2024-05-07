import random

list_of_favourite_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
print(list_of_favourite_fruits)

randomly_generated_fruit = random.choice(list_of_favourite_fruits)
print(randomly_generated_fruit)


def check_guess(guess_the_letter):
 
    if guess_the_letter in randomly_generated_fruit.lower():
        print(f'"Good guess! {guess_the_letter} is in the word")')
    
    else:
        print(f'"Sorry, {guess_the_letter} is not in the word. Try again")')


def ask_for_input():
    while True:  # let the code run continuosly 
        guess_the_letter = input("Guess the letter: ").lower() #.lower() applied directly to the input function

        if len(guess_the_letter) == 1 and guess_the_letter.isalpha():
            break

        else:   
            print("Invalid letter. Please, enter a single alphabetical character")
    check_guess(guess_the_letter)

    print("Good guess") #this can't be placed after the "break" as break means the loop has already exited and jumps to the next line of code

ask_for_input()



