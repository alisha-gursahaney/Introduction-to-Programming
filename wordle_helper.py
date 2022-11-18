# Name: Alisha Gursahaney
# Net Id: amg9zd

def create_dictionary():
    # Preprocess five-letter words into a full dictionary and common words list
    five_letter_dictionary = {}
    common_words_list = []
    file = open("five_letter_words.txt")
    for line in file:
        line = line.strip(" ,\n\r")
        if len(line) == 5:
            five_letter_dictionary[line] = ""
        else:
            line = line.strip("-")
            five_letter_dictionary[line] = ""
            common_words_list.append(line)
    return common_words_list, five_letter_dictionary

def make_empty_guess():
    return " \u0332 \u0332 \u0332  \u0332 \u0332 \u0332  \u0332 \u0332 \u0332  \u0332 \u0332 \u0332  \u0332 \u0332 \u0332"

def make_keyboard():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyboard = "QWERTYUIOP\n ASDFGHJKL\n   ZXCVBNM"
    # Initialize keyboard into light gray buttons
    for char in keyboard:
        if char in alphabet:
            keyboard = keyboard.replace(char, '\u001b[47;1m ' + char + ' \u001b[0m')
    return keyboard

def print_screen(guesses, keyboard):
    print()
    print("    " + guesses[0])
    print("    " + guesses[1])
    print("    " + guesses[2])
    print("    " + guesses[3])
    print("    " + guesses[4])
    print("    " + guesses[5])
    print()
    print(keyboard)

def make_button(letter, color):
    if color == "light_gray":
        return '\u001b[47;1m ' + letter + ' \u001b[0m'
    elif color == "dark_gray":
        return '\u001b[100;1m ' + letter + ' \u001b[0m'
    elif color == "yellow":
        return '\u001b[43;1m ' + letter + ' \u001b[0m'
    elif color == "green":
        return '\u001b[42;1m ' + letter + ' \u001b[0m'
