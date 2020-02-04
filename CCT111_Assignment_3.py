##############################################
# Author: Justin Sousa
# Class: CCT 111, Winter 2019
# Programming Assignment #3
# 11/15/19
#
# Description: This assignment involves coding and testing of a program that facilitates playing the Hangman word game. Hangman is a popular word game. In this game, the player is given some number of blanks representing the name of a movie or an actor and he/she has to guess the name using at most k number of chances.
# No sources to cite.
##############################################

import random

def user_Input_Valid(user_i):
        ''' Creating a function that will take in the users input and determine if is valid, according to the rules of the game, Hangman. This is done by using a series of if statements that will check: the length of the input, the type of input, and if the input the gave is "Legal". Depending on the outcome of the if-statements is the input is deemed valid then the function will return a value of True, and if deemed invaled then it will return a value of False. '''
       
        illegal_characters = ['`', '~', '!', '@', '#','$','%','^','&','*','(',')','_','-','=','+','[','{',']','}',"'\'",'|',':',';',',','<','>','.','/','?']
        
        if user_i in illegal_characters:
                print("Not a valid character. Please enter a valid character.")
                return False
        if len(user_i) != 1 and user_i.isdigit() == True:        
                print("Please enter one, and only one valid character.")
                return False
        elif  len(user_i) != 1 and user_i.isdigit() == False:
                print("Please enter only one valid character")
                return False
        elif len(user_i) == 1 and user_i.isdigit() == True:
                print("This is not a valid letter. Please enter a valid one")
                return False
        else:
                return True        
        
''' Getting the file that contains the words that will selected to be guessed at random. It will try to obatin the contents of the file, if successful then it will loop through the lines of the txt file and seperatae by lines then by words, appending it to a list called guessing_words. If the file cannot be obtained then it will print out the message "File cannot be opened:', fname" with fname being the name of the file. '''
fname = "Assignment_3_Words.txt"
guessing_words = []

try:
        script_words = open(fname, encoding ="utf8" )
except:
        print('File cannot be opened:', fname)
        exit()
        
for line in script_words:
        words = line.split()
        words.sort()
        for word in words:
                guessing_words.append(word)
                
random_word = random.choice(guessing_words)
print(random_word)
secert_word = []
display_word = []
num_guesses = 10
wrong_guesses = ''
correct_guesses = []
num_guesses =  10

''' Is used for setting the the word that is going to be guessed by looping through it can replaceing every letter with and underscore (_). '''
for c in random_word:
        secert_word.append(c)
        random_word = random_word.replace(c, "_")        
        display_word = list(random_word)


''' Creating a while loop that will check if the users remaing number of guesses is not equal to 0. If not then i will run through a series of if statements that will determine if the input given - the character - is in the word they are trying to guess, along side if it has been guessed before and displaying the appropiate output for each respective scenario. If the user has 0 remaining guesses then it will output that the user has lost the game, aswell as the word they were trying to guess. '''
while num_guesses !=  0 :
        ''' Formating the formal output. '''
        print("\nChances Remaining: ", num_guesses, )
        print("Missed Letters are: " , *wrong_guesses, sep = ' ')
        print(*display_word, sep = ' ')
        user_input = input('Enter a guess (one letter only). ').lower()
        
        if user_Input_Valid(user_input) == True:
                if user_input not in correct_guesses and user_input.lower() in secert_word or user_input.upper() in secert_word:
                        correct_guesses.append(user_input)
                        change_letter = [i for i, e in enumerate(secert_word) if e.lower() == user_input]
                        counter = 0
                
                        while counter < len(change_letter):
                                display_word[change_letter[counter]] = secert_word[change_letter[counter]]
                                counter = counter + 1
                        
                                if secert_word == display_word:
                                        print("Congrats You Won!!!")    
                                        exit()
                                else:
                                        continue
        
                elif user_input not in secert_word and user_input not in wrong_guesses: 
                        print("Wrong!")
                        wrong_guesses = wrong_guesses + user_input
                        num_guesses = num_guesses - 1
                elif user_input in wrong_guesses: 
                        print("You already tried this letter. Guess again!")
                elif user_input in correct_guesses:
                        print("You already got this letter")        
        else:
                pass
        if num_guesses == 0:
                print("\nYou have lost!")
                display_word = secert_word
                print("\nThe Correct Word Was: ", *display_word, sep = ' ')
                exit()
