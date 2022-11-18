# Name: Alisha Gursahaney
# Net Id: amg9zd

'''
Bugs:
- Should be "range(5)" instead of "range(1,5)"
- Should be "guesses[guess_num-1] = color_guess" instead of "guesses[guess_num] = color_guess"
- The number of guesses is wrong when secret_word is guessed correctly - guess_num should only increment after an incorrect guess
    - Alternatively, the student could initialize guess_num to 0
- Should be "while guess_num <= 6" instead of "while guess_num < 6" (unless they initialize guess_num to 0)
- Should be "while not possible:" instead of "while possible:" - Allows while loop to ask for the secret_word, otherwise it won't run
- Remove guessed_correctly = False at end of while loop
- Elif case should replace with a yellow button (not dark grey) in the keyboard: "keyboard = keyboard.replace(light_button, yellow_button)"
- Bad indentation in else statement in function
- Picky bug: remember to replace any yellow letter with a green letter in keyboard in else case (this case is covered in an example run)
'''
import random
import wordle_helper

#Create dictionary and screen elements [DON'T CHANGE THIS SECTION]
common_words_list, five_letter_dictionary = wordle_helper.create_dictionary()
keyboard = wordle_helper.make_keyboard() #A string formatted into a keyboard
empty_guess = wordle_helper.make_empty_guess() #A string formatted to represent an empty guess
guesses = [empty_guess, empty_guess, empty_guess, empty_guess, empty_guess, empty_guess]

def enter_guess(guess, guess_num):
    '''
    Updates the screen colors (guesses and keyboard) to reflect the user's guess
    '''
    global secret_word, keyboard, guesses

    guess = guess.upper()
    color_guess = " "
    #Update keyboard and build color_guess
    for i in range(1, 5): #*** Should be range(5) ***
        letter = guess[i]

        # The buttons are just colored strings
        light_button = wordle_helper.make_button(letter, "light_gray")
        dark_button = wordle_helper.make_button(letter, "dark_gray")
        yellow_button = wordle_helper.make_button(letter, "yellow")
        green_button = wordle_helper.make_button(letter, "green")

        if letter.lower() not in secret_word:
            #Wrong letter
            color_guess += light_button + " "
            keyboard = keyboard.replace(light_button, dark_button)
        elif letter.lower() != secret_word[i]:
            #Correct letter wrong spot
            color_guess += yellow_button + " "
            keyboard = keyboard.replace(light_button, dark_button) #*** Should be "keyboard = keyboard.replace(light_button, yellow_button)" ***
        else: # *** This else case has bad indentation ***
                #Correct letter correct spot
                color_guess += green_button + " "
                keyboard = keyboard.replace(light_button, green_button)
                #*** Need to add in keyboard = keyboard.replace(yellow_button, green_button) here ***

    # Update guess list by replacing black guess with the
    guesses[guess_num] = color_guess #*** Should be guesses[guess_num-1] = color_guess unless they initialize guess_num to 0***


#Initialize game
randomize = input("Would you like to randomize your secret word (y/n)? ")
if randomize == "y" or randomize == "Y" or randomize == "yes" or randomize == "Yes":
    choice = random.randint(1, len(common_words_list)-1)
    secret_word = common_words_list[choice]
else:
    possible = False
    while possible: #*** Should be "while not possible:" ***
        secret_word = input("Please enter the secret word: ").lower().strip()
        possible = secret_word in five_letter_dictionary
        if not possible:
            print("Please enter a valid 5-letter word.")

#Begin gameplay
guess_num = 1 #*** Could choose to initialize to 0 ***
guessed_correctly = False
while guess_num < 6 and guessed_correctly is False: # Should be "while guess_num <= 6" unless guess_num initialized to 0
    wordle_helper.print_screen(guesses, keyboard)
    #Ask for a guess until a valid guess is given
    possible = False
    while not possible:
        guess = input("Please guess a word: ").lower().strip()
        possible = guess in five_letter_dictionary
        if not possible:
            print("Please enter a valid 5-letter word.")

    enter_guess(guess, guess_num)

    if guess == secret_word:
        guessed_correctly = True
    guessed_correctly = False #*** This has no reason to be here ***
    guess_num += 1 #*** Should put this in an else statement unless guess_num is initialized to 0 ***

#Game over
wordle_helper.print_screen(guesses, keyboard)
if guessed_correctly == True:
    print("\nYou won! You correctly guessed the word in " + str(guess_num) + "/6 tries!")
else:
    print("\nYou ran out of tries. The secret word was \"" + secret_word + ".\"")


# '''
# Bugs:
# - Should be "range(5)" instead of "range(1,5)"
# - Should be "guesses[guess_num-1] = color_guess" instead of "guesses[guess_num] = color_guess"
# - The number of guesses is wrong when secret_word is guessed correctly - guess_num should only increment after an incorrect guess
#     - Alternatively, the student could initialize guess_num to 0
# - Should be "while guess_num <= 6" instead of "while guess_num < 6" (unless they initialize guess_num to 0)
# - Should be "while not possible:" instead of "while possible:" - Allows while loop to ask for the secret_word, otherwise it won't run
# - Remove guessed_correctly = False at end of while loop
# - Elif case should replace with a yellow button (not dark grey) in the keyboard: "keyboard = keyboard.replace(light_button, yellow_button)"
# - Bad indentation in else statement in function
# - Picky bug: remember to replace any yellow letter with a green letter in keyboard in else case (this case is covered in an example run)
# '''
# import random
# import wordle_helper
#
# #Create dictionary and screen elements [DON'T CHANGE THIS SECTION]
# common_words_list, five_letter_dictionary = wordle_helper.create_dictionary()
# keyboard = wordle_helper.make_keyboard() #A string formatted into a keyboard
# empty_guess = wordle_helper.make_empty_guess() #A string formatted to represent an empty guess
# guesses = [empty_guess, empty_guess, empty_guess, empty_guess, empty_guess, empty_guess]
#
# def enter_guess(guess, guess_num):
#     '''
#     Updates the screen colors (guesses and keyboard) to reflect the user's guess
#     '''
#     global secret_word, keyboard, guesses
#
#     guess = guess.upper()
#     color_guess = " "
#     #Update keyboard and build color_guess
#     for i in range(1, 5): #*** Should be range(5) ***
#         letter = guess[i]
#
#         # The buttons are just colored strings
#         light_button = wordle_helper.make_button(letter, "light_gray")
#         dark_button = wordle_helper.make_button(letter, "dark_gray")
#         yellow_button = wordle_helper.make_button(letter, "yellow")
#         green_button = wordle_helper.make_button(letter, "green")
#
#         if letter.lower() not in secret_word:
#             #Wrong letter
#             color_guess += light_button + " "
#             keyboard = keyboard.replace(light_button, dark_button)
#         elif letter.lower() != secret_word[i]:
#             #Correct letter wrong spot
#             color_guess += yellow_button + " "
#             keyboard = keyboard.replace(light_button, dark_button) #*** Should be "keyboard = keyboard.replace(light_button, yellow_button)" ***
#         else: # *** This else case has bad indentation ***
#                 #Correct letter correct spot
#                 color_guess += green_button + " "
#                 keyboard = keyboard.replace(light_button, green_button)
#                 #*** Need to add in keyboard = keyboard.replace(yellow_button, green_button) here ***
#
#     # Update guess list by replacing black guess with the
#     guesses[guess_num] = color_guess #*** Should be guesses[guess_num-1] = color_guess unless they initialize guess_num to 0***
#
#
# #Initialize game
# randomize = input("Would you like to randomize your secret word (y/n)? ")
# if randomize == "y" or randomize == "Y" or randomize == "yes" or randomize == "Yes":
#     choice = random.randint(1, len(common_words_list)-1)
#     secret_word = common_words_list[choice]
# else:
#     possible = False
#     while possible: #*** Should be "while not possible:" ***
#         secret_word = input("Please enter the secret word: ").lower().strip()
#         possible = secret_word in five_letter_dictionary
#         if not possible:
#             print("Please enter a valid 5-letter word.")
#
# #Begin gameplay
# guess_num = 1 #*** Could choose to initialize to 0 ***
# guessed_correctly = False
# while guess_num < 6 and guessed_correctly is False: # Should be "while guess_num <= 6" unless guess_num initialized to 0
#     wordle_helper.print_screen(guesses, keyboard)
#     #Ask for a guess until a valid guess is given
#     possible = False
#     while not possible:
#         guess = input("Please guess a word: ").lower().strip()
#         possible = guess in five_letter_dictionary
#         if not possible:
#             print("Please enter a valid 5-letter word.")
#
#     enter_guess(guess, guess_num)
#
#     if guess == secret_word:
#         guessed_correctly = True
#     guessed_correctly = False #*** This has no reason to be here ***
#     guess_num += 1 #*** Should put this in an else statement unless guess_num is initialized to 0 ***
#
# #Game over
# wordle_helper.print_screen(guesses, keyboard)
# if guessed_correctly == True:
#     print("\nYou won! You correctly guessed the word in " + str(guess_num) + "/6 tries!")
# else:
#     print("\nYou ran out of tries. The secret word was \"" + secret_word + ".\"")