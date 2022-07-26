
from random_word import RandomWords
r = RandomWords()
from hangman_art import stages, logo 
import os

# clear console screen 
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# START
print(f" {logo}\n\nLet's play hangman! You must guess the random word selected in this game.\n")

# generate random word
chosen_word_unformatted = r.get_random_word(hasDictionaryDef="true")
   # change to lower case and remove any hyphens
chosen_word = chosen_word_unformatted.replace("-", "").lower()
display = []

# display blank spaces for each letter in chosen word
for char in chosen_word:
   display.append("_")

lives = 7
win = False
wrong_guesses = [] 

# loop through game as long as user hasn't won or lost yet
while lives > 0 and win != True:
   print(stages[lives])
   if lives < 7:
      print(f"Wrong guesses: {', '.join(wrong_guesses)}\n")
   print(f"{' '.join(display)}\n")
   guess = input("Enter a letter\n").lower()
   clear()
   # replace blank space in display with correct letter
   for position in range(len(chosen_word)):
      if guess == chosen_word[position]:
         display[position] = guess
         if "_" not in display:
            print(f"You win!\n{' '.join(display)}")
            print(logo)
            win = True

   # if user guessed wrong, draw hangman and lose life 
   if guess not in chosen_word:
      lives -= 1
      wrong_guesses += guess
      print(f"{guess} is not in the word. You lose a life.\n")
      if lives == 0:
         print(logo)
         print(f"You lose! The word was \"{chosen_word}\"")
         print(stages[lives])

