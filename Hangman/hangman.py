import random
from words import words #Importing the word list
import string

lives = 3 #Can be any other value

def get_valid_word(words): #In case user inputs words in the word file which become invalid
    word = random.choice(words) #Random choice from our predefined list
    return word

def hangman():
    word = get_valid_word(words) #Can be commented out
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase) #Initializing a set
    used_letters = set() #What the user has guessed

    while len(word_letters) > 0 and lives > 0:
        #We'll do everything in UPPERCASE

        print("You have used these letters: ", " ".join(used_letters)) #Joining the used letters set with a space

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("The current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives = lives - 1 #We remove a life for every incorrect guess
                print(f"Letter is not in the word, try again. You have {lives} lives remaining. ")

        elif user_letter in used_letters:
            print("You have already used that letter. ")

        else:
            print("Invalid character input.")

if lives == 0:
    print(f"You died, the word was {word}. ")
else:
    print("You guessed the word correctly! ")