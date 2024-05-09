import random
list_of_favourite_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
print(list_of_favourite_fruits)

randomly_generated_fruit = random.choice(list_of_favourite_fruits)
print(randomly_generated_fruit)

class Hangman():
    def __init__(self, randomly_generated_fruit, word_guessed, num_letters, list_of_favourite_fruits, list_of_guesses=[], num_lives=5 ):
        self.randomly_generated_fruit = randomly_generated_fruit
        self.word_guessed = word_guessed
        self.num_letters = num_letters   
        self.list_of_favourite_fruits = list_of_favourite_fruits
        self.list_of_guesses = list_of_guesses
        self.num_lives = num_lives

        def check_guess_in_word(guess):

            word_guessed  = ["_"] * len(randomly_generated_fruit)  # represents the current state of the word being guessed with "_" representing letters that haven't been guessed yet
 
            if guess in randomly_generated_fruit.lower():
                print(f'"Good guess! {guess} is in the word")')

            #loop through the letters in randomly_generated_fruit
            #index tells us the position of the current character within the word
            for index, letter in enumerate(randomly_generated_fruit):
                #check if the current looped letter is equal to the guess
                if letter == guess:
                    #set the underscore at that position to the correct letter
                    word_guessed[index] = letter
                
                else:
                    num_lives -- 1
                    print("Sorry, {letter} is not in the word")
                    print("You have {num_lives} lives left")

        num_letters -- 1

        def ask_for_valid_user_input():
            while True:  # let the code run continuosly 
                guess = input("Guess the letter: ").lower() #.lower() applied directly to the input function

                if len(guess) != 1 and not guess.isalpha():
                    print("Invalid letter. Please, enter a single alphabetical character")
                
                elif guess in list_of_guesses:
                    print( "You already tried that letter")
    
                else:
                    check_guess_in_word(guess)
                    list_of_guesses.append(guess)
                    break   # to break out of the loop
        
        ask_for_valid_user_input()