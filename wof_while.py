# Name: Alisha Gursahaney
# Net Id: amg9zd

# Name: Alisha Gursahaney
# Net Id: amg9zd
# Partners: Prajwala Sinha ps3frx and Mark Provost map5xnk

word = input("Enter a word or phrase: ")
print(f"The word to guess: {len(word) * '_'}")
hidden_word = len(word) * '_'
guess = input("Guess a letter: ")
find = word.find(guess)


def guessing():
    if word.count(guess) > 0:
        def replace():
            if word.count(guess) >= 1:
                if word.count(guess) == 1:
                    global hidden_word
                    replace = hidden_word[0:find] + guess + hidden_word[find + 1:len(word) + 1]
                    hidden_word = replace
                    return hidden_word
                else:
                    def multiple_replace():
                        global hidden_word
                        global find
                        replace = hidden_word[0:find] + guess + hidden_word[find + 1:len(word) + 1]
                        hidden_word = replace
                        find_again = word.find(guess, find + 1, len(word))
                        find = find_again
                        replace = hidden_word[0:find] + guess + hidden_word[find + 1:len(word) + 1]
                        hidden_word = replace
                        return find, hidden_word

                    word.count(guess) * multiple_replace()
                    return hidden_word

        replace()
    else:
        return hidden_word


while hidden_word.count('_') >= 1:
    guessing()
    print(f"The word to guess: {hidden_word}")
    guess = input("Guess a letter: ")
    find = word.find(guess)
    #replace = hidden_word[0:find] + guess + hidden_word[find + 1:len(word) + 1]

print(f"The word to guess: {word}")

