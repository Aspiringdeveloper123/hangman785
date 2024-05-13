import random
list_of_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
randomly_generated_fruit = random.choice(list_of_fruits)
print(randomly_generated_fruit)

class Hangman():
    '''
    This class is used to represent the Hangman game

    Attributes:
        randomly_generated_fruit(str) = word to be guessed which is randomly generated from the "list of fruits" list
        word_guessed(list) = a list of the letters for the word, initialised with underscores
        num_letters(int) = number of unique letters in the word that has not been guessed yet  
        list_of_fruits(list) = list of fruits from which the word to be guessed is randomly chosen
        list_of_guesses(list) = list of guesses that the user has already tried
        num_lives(int) = number of lives at the start of the game

    '''
    def __init__(self, list_of_fruits, list_of_guesses=[], num_lives=5 ):  
        '''
        Initialise the Hangman game.

        Args:
            list_of_fruits(list) = list of fruits from which the word to be guessed is randomly chosen
            list_of_guesses(list) = list of guesses that the user has already tried
            num_lives(int) = number of lives at the start of the game
        
        
        '''
        # lower() converts the word to lowercase immediately
        # self.word_guessed and self.num_letters is a class variable which has been assigned a value

        self.randomly_generated_fruit = random.choice(list_of_fruits).lower()  
        self.word_guessed = ["_"] * len(self.randomly_generated_fruit)   
        self.num_letters = len(set(randomly_generated_fruit))  
        self.list_of_fruits = list_of_fruits
        self.list_of_guesses = list_of_guesses 
        self.num_lives = num_lives

        # indent this print statement
        print("Letters in the word to be guessed:", self.word_guessed) 

    # Args = the arguments the method takes, in this case, none
    # Returns = the value or values the method returns. If nothing is returned, it's often stated as "None"

    def _play_game(self):
        '''
        This function represents the start of the Hangman game

        Returns:
            str: "Congratulations. You won the game!" if there are no more letters to be guessed and the number of lives is more than 0
                 "You lost!" if the number of lives reaches 0 before guessing all letters
            
            The purpose of this function is to inform the user how many lives they have. 
            When the number of lives reaches 0, the user has lost
            When the number of lives is more than 0, the user will be prompted to enter another letter as a guess
            When there are no remaining letters to be guessed and the user's lives are more than 0, the user has won the game
        
        '''
        print(self.list_of_fruits)
    
        while True:
            if self.num_lives == 0:
                print("You lost!")
                # add a return so it will end the while True, can't just have a print statement
                return 
               
            
            elif self.num_letters > 0 and self.num_lives > 0:
                self._ask_for_valid_user_input()

            elif not self.num_lives == 0 and self.num_letters < 1:
                print("Congratulations. You won the game!")
                return
               
    def _check_guess_in_word(self, guess):   
        '''
        This function is used to check if the guessed letter (`guess`) is present in the word to be guessed. 

        Args: 
            guess (str): The guessed letter

        Returns: 
            str: "Good guess! {guess} is in the word" if the letter is in the word and updates the corresponding position
            in the word_guessed list with the correct letter  
            str: "Sorry, {guess} is not in the word" if the guessed letter is not in the word
            str: "You have {self.num_lives} lives left" states how many lives are left after each time the user guesses the letter incorrectly
        '''
        print(self.randomly_generated_fruit)
        current_fruit = self.randomly_generated_fruit.lower()
        if guess in current_fruit:
            print(f'"Good guess! {guess} is in the word")')
       
            # create a for loop which loops through the letters in current_fruit
            # enumerate gets us the index and corresponding character during each iteration
            # index tells us the position of the current character within the word
            for index, letter in enumerate(current_fruit):
                
                # check if the current looped letter in the word matches the guessed letter (guess)
                if letter == guess:
                    # update the corresponding position in the word_guessed list with the correct letter.
                    # the index variable tells us the position of the current letter in the word
                    self.word_guessed[index] = letter 
            # captures guesses that are not already in the list     
            self.list_of_guesses.append(guess) 
            # print after the loop to show the current state of the word
            print(self.word_guessed)  
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
           

   # this is already been accessed in the play_game method so you don't need to call this method again otherwise this will make it a recursive method
    def _ask_for_valid_user_input(self):  
        '''
        This function is used to ask for valid user input for a single alphabetical character and to check if the guess has already been made

        Returns: 
            str: ""Guess the letter: " to ask for the user to enter a letter 
            str: "Invalid letter. Please, enter a single alphabetical character" if the user does not put an alphabetical character
            str: "You already tried that letter" if the user has already made that guess
                
        '''
        # let the code run continuosly 
        while True:  
            # .lower() applied directly to the input function
            guess = input("Guess the letter: ").lower() 

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print( "You already tried that letter")
            else:
                # runs the code in the method seen in "check_guess_in_word"
                self._check_guess_in_word(guess) 
                break
           
 
num_lives = 5
list_of_fruits = ["Strawberry", "Watermelon", "Mango", "Pineapple", "Kiwi"]
# create an instance of the class, to call the class
game = Hangman(list_of_fruits)    
game._play_game()






