# random is similar to math.floor(math.random)
import random

# create a list of words to randomize for game play
word_list = [
    'soup',
    'mountain',
    'coding',
    'teaching',
    'expert',
    'python',
    'javascript',
    'games',
    'pizza',
    'tacos',
    'banana',
    'chicken',
    'dancing',
    'songwriter',
    'coin',
    'throw',
    'silence',
    'catch',
    'running',
    'climb'
]

# create a Word class to instantiate each new word
class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        # player has 8 chances to guess the word
        self.guesses = 8
        # make a list of dashes that is the length of the chosen word
        self.word_to_dashes = list('_' * len(self.chosen_word))
        # this method will split the word up into a list of dictionaries with 2 attributes:
        # the letter/character, and a boolean representing whether or not it has been guessed
        # self.word_to_dicts = []
    
    # def split_word(self, word):
    #     print(word)
    #     self.word_to_dicts.append({char, False} for char in word)
    #     print(self.word_to_dicts)
    #     # return [{char, False} for char in word]  
    # COULDN'T FIGURE THIS OUT. NEED TO KEEP TRYING
    
    
    def get_letter_index(self, letter):
        # enumerate() will count and provide the index for each character simultaneously
        # this function will return the index for each character in the word where the letter that was input matches in an array
        # it only returns the index/indices if the letter that was input matches the character in the loop
        return [i for i, char in enumerate(self.chosen_word) if letter == char]
        # this way you can use that index/indices to send to the check_progress function
    
    
    def check_progress(self, letter, indices):
        # Update the word_to_dashes with the guessed letters
        # you'll need the letter that should be added to the dashes within the word_to_dashes list
        # you'll need to look at the indices of each letter in the chosen word and then update the indices that match the letter
                     
        # loop through all the indices
        for index in indices:
            # Switch the individual index from a '_' to the letter if it matches 
            self.word_to_dashes[index] = letter

    def play(self):
        # while the player still has guesses 
        while self.guesses > 0:
            # show the word_to_dashes array which has the dashes matching the word length
            print('\n')
            print(self.word_to_dashes)
            print('\n')
            # ask for a letter to inpute
            user_input = input('\nPlease type a letter: ')
            # Check if the letter is not already guessed
            if user_input in self.word_to_dashes:
                print('You already have guessed that letter')
                continue
            # If the letter is in the word
            if user_input in self.chosen_word:
                # Print a correct message
                print('Yes!',(user_input).upper(),'is in the word.')
                print('You have {} remaining guesses'.format(self.guesses))
                # store the indices of all the matching corresponding letters that are returned from the get_letter_index function for that letter
                indices = self.get_letter_index(user_input)
                # send the indices array to check_progress function so the word_to_dashes array is updated with the newly included letters
                self.check_progress(user_input, indices)
            # Otherwise, tell the player the letter is not in the word
            else:
                print(user_input.upper(),'is not in the word.')
                # remove a guess since it was incorrect
                self.guesses -= 1
                print('You have {} remaining guesses'.format(self.guesses))
                
                
            # If the word has been guessed and there are no more empty dashes in the word_to_dashes array
            if self.word_to_dashes.count('_') == 0:
                # show the final word and have a win message
                print('\n')
                print(self.word_to_dashes)
                print('\n')
                print('\nCongrats, you guessed the word! You win!')
                print('The word is: {}'.format(self.chosen_word))
                # quit the running of the python file
                quit()
            
        # If there are no more guesses available and they still have not completed the word
        if self.guesses == 0:
            # show a lose message with the final word
            print("\nSorry, you ran out of tries. The word was " + self.chosen_word + ". Maybe next time!")
            quit()
        
        
        
# Python interpreter reads a source file, sets special __name__ variable and executes all of the code
if __name__ == '__main__':
    # The choice() method returns a randomly selected element from the specified sequence
    # set the word before starting the game
    chosen_word = random.choice(word_list)
    # create a new instantiation of Word class using the random word from the list
    # Store it in a variable
    word = Word(chosen_word)
    # execute the play function that is created within the class 
    word.play()

# new_word = Word('hello')
# new_name = new_word.chosen_word
# print(new_word)
# new_word.split_word(new_name)