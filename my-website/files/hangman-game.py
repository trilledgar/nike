import sys # imports the system module
import random # imports the random module
global turns # makes the turn variable global
global c_guesses # makes the c_guesses variable global
global status # makes the variable status global
global word # makes the variable word global
global check # makes the variable check global
word_list = ['word','apples','oranges','people','hangman','random','pie','google','pizza','good','food','hello','flip','happy','what','bruh','spiderman','superman','everybody','dude','lose','win','soccer','basketball','venom','python','homework','science','engineering','school','highschool'] # sets the variable word_list as a list of strings(words)
word = list(random.choice(word_list)) # sets the variable word as a random choice from word_list, but as a string
turns = (6) # sets the variable turns as the integer 6
c_guesses = [] # sets the variable c_guesses as an empty list
status = [] # sets the variable status as an empty list
check = [] # sets the variable check as an empty list

def greeting(): # defines the function greeting
    print ('Hello there,')
    playornah()
    
def playornah(): # defines the function playornah
    print ('Would you like to play Hangman?')
    answer = raw_input() # sets the variable as the raw_input
    print ('\n' * 3)
    answer = answer.lower() # sets the variable answer as answer but lowercase
    if answer=='yes': # checks if the variable answer is yes
        play() # calls on the function play
    elif answer=='no': # checks if the variable answer is no
        nah() # calls on the function nah
    else:
      print ('Not an option.')
      playornah() # calls on the function playornah
    
def nah(): # defines the variable nah
    print ('Okay then, goodbye.')
    sys.exit() # calls on the function sys.exit to stop the program
    
def play(): # defines the variable play
    global c_guesses # calls on the variable c_guesses
    global status # calls on the variable status
    global word # calls on the variable word
    global check # calls on the variable check
    status = '' # sets the variable status as a string
    if turns <= 0: # Checks if the variable turns is equal to or less than 0
       status = '' # sets the variable status as a string
       for letter in word: # for every letter in word
            status += letter # adds the letter to status
       print ('  _________\n |         |\n |         0\n |        /|\ \n |        / \ \n |\n |\n')
       print ('Game Over')
       print 'The word was', status, '.'
       gameover() # calls on the function gameover
    if turns == 1: # Checks if the variable turns is equal to 1
       print ('  _________\n |         |\n |         0\n |        /|\ \n |        /   \n |\n |\n') 
    if turns == 2: # Checks if the variable turns is equal to 2
       print ('  _________\n |         |\n |         0\n |        /|\ \n |            \n |\n |\n') 
    if turns == 3: # Checks if the variable turns is equal to 3
       print ('  _________\n |         |\n |         0\n |        /|  \n |            \n |\n |\n') 
    if turns == 4: # Checks if the variable turns is equal to 4
       print ('  _________\n |         |\n |         0\n |         |  \n |            \n |\n |\n') 
    if turns == 5: # Checks if the variable turns is equal to 5
       print ('  _________\n |         |\n |         0\n |            \n |            \n |\n |\n') 
    if turns == 6: # Checks if the variable turns is equal to 6
       print ('  _________\n |         |\n |          \n |            \n |            \n |\n |\n') 
    for letter in word: # for every letter in the list word
        if letter in c_guesses: # if the letter is in the list c_geusses
            status += letter # adds the letter to the string status
        else:
            status += '-' # adds the string '-'
    print (status)
    check = list(status) # sets the variable check as a list of the variable status
    answer = raw_input('Whats your guess?\n') # sets the variable answer as raw input
    guess = answer.lower() # sets the variable geuss as the variable answer but lowercase
    print ('\n' * 3)
    if guess in word: # checks if geuss is in the list word
        c_guesses += ((guess) * (word.count(guess))) # adds the variable guess to c_geusses as many times it apears in the word
        print 'Correct, it appears', word.count(guess), 'times.\n'
        if len(c_guesses) == len(word): # checks if the length of c_guesses is equal to the length of word
            status = '' # sets the variable status as a string
            for letter in word: # for every letter in word
                status += letter # adds the letter to status
            print 'The word was',status 
            win() # calls on the function win
        else:     
            correct() # calls on the function correct
    else:
        wrong() # calls on the function wrong
        
def correct(): # defines the function correct
    play() # calls on the function play

def wrong(): # defines the function wrong
    global turns # calls on the variable turns
    print ('wrong')
    turns -= 1 # subtracts 1 from the variable turns
    if turns == 6 or 5 or 4 or 3 or 2 or 1: # checks if the variable turns is equal to 6, 5, 4, 3, 2, or 1
        play() # calls on the function play
    else:
        gameover() # calls on the function gameover 
    
def gameover(): # defines the function gameover
    global turns# calls on the function gameover 
    global c_guesses # calls on the variable c_guesses
    global word # calls on the variable word
    print ('Would you like to play again?')
    answer =raw_input() # sets the variable answer as raw input
    print ('\n' * 3)
    answer = answer.lower() # sets the variable answer as answer but lowercase
    if answer=='yes': # checks if the variable answer is the string yes
        turns = 6 # sets the variable turns as the integer 6
        c_guesses = [] # sets the variable c_guesses as an empty list
        word = list(random.choice(word_list)) # sets the variable word as a random choice from word_list, but as a list
        play() # calls on the function play
    elif answer=='no': # checks if the variable answer is the string no
        nah() # calls on the function nah
    else:
      print ('Not an option')
      gameover() # calls on the function gameover 
    
def win(): # defines the function win
    global turns # calls on the function gameover 
    global c_guesses # calls on the variable c_guesses
    global word # calls on the variable word
    print ('You win!')
    print ('Would you like to play again?')
    answer =raw_input() # sets the variable answer as raw input
    print ('\n' * 3)
    answer = answer.lower() # sets the variable answer as answer but lowercase
    if answer=='yes': # checks if the variable answer is the string yes
        turns = 6 # sets the variable turns as the integer 6
        c_guesses = [] # sets the variable c_guesses as an empty list
        word = list(random.choice(word_list)) # sets the variable word as a random choice from word_list, but as a list
        play() # calls on the function play
    elif answer=='no': # checks if the variable answer is the string no
        nah() # calls on the function nah
    else:
      print ('Not an option')
      win() # calls on the function win
     
greeting() # calls on the function greeting
