import random
list_of_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
print(list_of_fruits)

randomly_generated_fruit = random.choice(list_of_fruits)
print(randomly_generated_fruit)

class Hangman():
    '''
    This class is used to represent the Hangman game

    Attributes:
        randomly_generated_fruit = word to be guessed which is randomly generated from the "list of fruits" list
        word_guessed(list) = a list of the letters for the word
        num_letters(int) = number of unique letters inthe word that has not been guessed yet  
        list_of_fruits(list) = list of fruits
        list_of_guesses(list) = list of guesses that the user has already tried
        num_lives(int) = number of lives at the start of the game

    '''
    def __init__(self, randomly_generated_fruit, num_letters, list_of_fruits, list_of_guesses=[], num_lives=5 ):
      
        self.randomly_generated_fruit = randomly_generated_fruit
        self.num_letters = num_letters   
        self.list_of_fruits = list_of_fruits
        self.list_of_guesses = list_of_guesses
        self.num_lives = num_lives


        def initialise_word_guessed(self):
             # create/ initialise a list of underscores, with each underscore representing a letter in the word to be guessed
             # use self so that the "word_guessed" attriute can be accessed by other methods within the class (e.g _check_guess_in_word)
             # remove attribute in the __init__ method
            self.word_guessed  = ["_"] * len(self.randomly_generated_fruit) 

        def _check_guess_in_word(self, guess):

            #check if the guessed letter (`guess`) is in the word to be guessed
            if guess in randomly_generated_fruit.lower():
                print(f'"Good guess! {guess} is in the word")')
       
            # create a for loop which loops through the letters in randomly_generated_fruit
            #enumerate gets us the index and corresponding character during each iteration
            #index tells us the position of the current character within the word
                for index, letter in enumerate(randomly_generated_fruit):
                    #check if the current looped letter in the word matches the guessed letter (guess)
                    if letter == guess:
                    # update the corresponding position in the word_guessed list with the correct letter.
                    # the index variable tells us the position of the current letter in the word
                        self.word_guessed[index] = letter 
                
                    else:
                        self.num_lives -= 1
                        print("Sorry, {guess} is not in the word")
                        print("You have {num_lives} lives left")
                    self.num_letters -= 1

        def _ask_for_valid_user_input(self):
            while True:  # let the code run continuosly 
                guess = input("Guess the letter: ").lower() #.lower() applied directly to the input function
                if validate_guess and not already_guessed:
                    self.check_guess_in_word(guess)  #then runs the code in the method - "check_guess_in_word"
                    self.list_of_guesses.append(guess)
                break   # to break out of the loop
        
        def validate_guess(self, guess):   #need to condition to explain what happens when this condition is true (seen above)
            if len(guess) != 1 or not guess.isalpha():
                    print("Invalid letter. Please, enter a single alphabetical character")

        def already_guessed(self,guess):     
            if guess in self.list_of_guesses:
                    print( "You already tried that letter")

            ask_for_valid_user_input()