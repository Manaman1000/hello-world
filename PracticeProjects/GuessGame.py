## SECRET WORD GUESSING GAME
## GOAL: Create a game where we store a secret word in the program, and allow the user to continually input words until they guess 
##        the correct word.
## PURPOSE: Demonstrate and practice using variables, while loops, if/elif/else statements

secret_word = "Giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Guess what word I am thinking of!")

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count+=1
    else:
        out_of_guesses = True


if out_of_guesses:    
    print("You ran out of guesses! You lost...")
else:
    print("You win!")
