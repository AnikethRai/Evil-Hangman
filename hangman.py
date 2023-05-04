import random
import string
from words import words
from hangy_print import checking_lives,congo

#Taking number of words and placing them in a list.
def valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word                 

def hangman(name):
    lives = 6
    print(f'\nYou have {lives} lives. Use them wisely.')
    word = valid_word().upper()
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()
    
    print('\nThe Randomly Generated Word length is as follows:')
    for i in range(len(word)):
        print('',end = '_ ')
    print('\nYour Guessing starts Now! \n')
    
    #logic
    while len(word_letters) > 0 and lives > 0:
        print(f'\n You have {lives} lives. And you have used these letters: ', ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word : ', ' '.join(word_list))
        
        user_guess = input('Guess a letter: ').upper()
        if user_guess in alphabets - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
            else:
                lives -= 1
                checking_lives(lives,name)
                
        elif user_guess in used_letters:
            print(f'{user_guess} is already used. Guess again')
        else:
            print('Invalid character!')
    if lives == 0:
        print('\n Anyways ................ \n')
        print(f'You are out of lives. The Word was {word}')
        print(f'Thank you for playing {name}')
        print('\n\n')
    else:
        print(f'Congragulations! you have guessed the word ! It is {word}')
        print(f'Thank you for playing {name}')
        print('\n\n')
        congo(name)


    
            
            
    

#Introduction
print('*'*100)
print('\nWelcome to the game of Evil Hangman\n')
print('\nHow to play ?\n')
print('\n1. You are given 6 lives and you have to guess the word within these six lives.')
print('2. If the letter you guess is not in the word then the life is taken away and if you guessed it right then your life stays the same.')
print('3. To Win you have to guess the right word!')
print('\n Good Luck!\n')
print('*'*100)

#User name
name = input('\n To start the game please Enter your Name: ')
print(f'\n Hello {name}, Let us start the game.')
hangman(name)
