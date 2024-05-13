import random
list_of_fruits = ["Kiwi"]
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

    
    def __init__(self, list_of_fruits, list_of_guesses=[], num_lives=5 ):  #that game needs to run the player puts in
      
        self.randomly_generated_fruit = random.choice(list_of_fruits).lower()  #add lower to convert the word to lowercase immediately
        self.word_guessed = ["_"] * len(self.randomly_generated_fruit)   #class variable which has been assigned a value
        self.num_letters = len(set(randomly_generated_fruit))  
        self.list_of_fruits = list_of_fruits
        self.list_of_guesses = list_of_guesses 
        self.num_lives = num_lives

        print("Letters in the word to be guessed:", self.word_guessed)  #this is indented

    def _play_game(self):
        '''
        This function represents the start of the Hangman game

        Args:
            num_lives (int) : number of lives

        Returns:
            str: "Congratulations. You won the game!" if there are no more letters to be guessed and the number of lives is more than 0
        
            The purpose of this function is to inform the user how many lives they have. 
            When the number of lives reaches 0, the user has lost
            When the number of lives is more than 0, the user will be prompted to enter another letter as a guess
            When there are no remaining letters to be guessed and the user's lives are more than 0, the user has won the game
        
        '''

        print(self.list_of_fruits)
    
    
        while True:
            if self.num_lives == 0:
                print("You lost!")
                return #add a return so it will end the while True, can't just have a print statement
               
            
            elif self.num_letters > 0 and self.num_lives > 0:
                self._ask_for_valid_user_input()

            elif not self.num_lives == 0 and self.num_letters < 1:
                print("Congratulations. You won the game!")
                return
               
  

    def _check_guess_in_word(self, guess):   
        '''
        This function is used to check  if the guessed letter (`guess`) is present in the word to be guessed. 

        Returns: 
            str: "Good guess! {guess} is in the word" if the letter is in the word and updates the corresponding position
            in the word_guessed list with the correct letter  

        '''
        print(self.randomly_generated_fruit)
        current_fruit = self.randomly_generated_fruit.lower()
        if guess in current_fruit:
            print(f'"Good guess! {guess} is in the word")')
       
            # create a for loop which loops through the letters in randomly_generated_fruit
            #enumerate gets us the index and corresponding character during each iteration
            #index tells us the position of the current character within the word
            for index, letter in enumerate(current_fruit):
                
                #check if the current looped letter in the word matches the guessed letter (guess)
                if letter == guess:
                    # update the corresponding position in the word_guessed list with the correct letter.
                    # the index variable tells us the position of the current letter in the word
                    self.word_guessed[index] = letter 
            self.list_of_guesses.append(guess) #captures guesses that are not already in the list hence it says "and not"
            print(self.word_guessed)  #printed after the loop to show the current state of the word
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} lives left")
           

   # this is already been accessed in the play_game method so you don't need to call it again- ask_for_valid_user_input as this will make it a recursive function
   
    def _ask_for_valid_user_input(self):  
        '''
        This function is used to ask for valid user input, ensuring it's a single alphabetical character and to check if the guess has already been made

        Returns: Nothing specific
                
        '''
        while True:  # let the code run continuosly 
            guess = input("Guess the letter: ").lower() #.lower() applied directly to the input function

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print( "You already tried that letter")
            else:
                self._check_guess_in_word(guess) #then runs the code in the method seen in "check_guess_in_word"
                break
           
 
num_lives = 5
list_of_fruits = ["Kiwi"]
game = Hangman(list_of_fruits)   #instance of the class, to call the class 
game._play_game()






