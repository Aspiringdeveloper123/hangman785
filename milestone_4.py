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
        num_letters(int) = number of unique letters in the word that has not been guessed yet  
        list_of_fruits(list) = list of fruits
        list_of_guesses(list) = list of guesses that the user has already tried
        num_lives(int) = number of lives at the start of the game

    '''
    def __init__(self, randomly_generated_fruit, word_guessed, num_letters, list_of_fruits, list_of_guesses=[], num_lives=5 ):
      
        self.randomly_generated_fruit = randomly_generated_fruit
        self.word_guessed = word_guessed
        self.num_letters = num_letters   
        self.list_of_fruits = list_of_fruits
        self.list_of_guesses = list_of_guesses 
        self.num_lives = num_lives


        def initialise_word_guessed(self):
             # use self so that the "word_guessed" attriute can be accessed by other methods within the class (e.g _check_guess_in_word)
            self.word_guessed  = ["_"] * len(self.randomly_generated_fruit) 
        '''
            This function initialises a list of underscores for the chosen word

            Returns:
                A list created with each underscore representing a letter in the word to be guessed
        
        '''

        def _check_guess_in_word(self, guess):
        
            '''
            This function is used to check  if the guessed letter (`guess`) is present in the word to be guessed

            Returns: 
                str: "Good guess! {guess} is in the word" if the letter is in the word and updates the corresponding position in the word_guessed list with the correct letter  
            '''
        
            if guess in self.randomly_generated_fruit.lower():
                print(f'"Good guess! {guess} is in the word")')
       
            # create a for loop which loops through the letters in randomly_generated_fruit
            #enumerate gets us the index and corresponding character during each iteration
            #index tells us the position of the current character within the word
                for index, letter in enumerate(self.randomly_generated_fruit):
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

            '''
            This function is used ask for valid user input

            Returns: 
                 If input is valid, the letter will be appended to the list_of_guesses
            '''

            while True:  # let the code run continuosly 
                guess = input("Guess the letter: ").lower() #.lower() applied directly to the input function
                if validate_guess and not already_guessed:
                    self.check_guess_in_word(guess)  #then runs the code in the method - "check_guess_in_word"
                    self.list_of_guesses.append(guess) #captures guesses that are not already in the list hence it says "and not"
                break   # to break out of the loop
        
        def validate_guess(self, guess):   #need to condition to explain what happens when this condition is true (seen above)
            
            '''
            This function is used to validate the guess, to ensure it's a single alphabetical character

            Returns: 
                str: "Invalid letter. Please, enter a single alphabetical character" 
            '''
            
            if len(guess) != 1 or not guess.isalpha():
                    print("Invalid letter. Please, enter a single alphabetical character")

        def already_guessed(self,guess):  
            
            '''
            This function is to let the user know they have already entered a letter tried previously

            Returns: 
                str: "You already tried that letter"
            '''
            if guess in self.list_of_guesses:
                    print( "You already tried that letter")

        ask_for_valid_user_input()