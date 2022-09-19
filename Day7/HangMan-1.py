import random
import Hangman_words
import Hangman_art
chosen_word = random.choice(Hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
print(Hangman_art.logo)
print(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter please: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
# print(guess)
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    print(f"{' '.join(display)}")
    if "_" not in display: 
        end_of_game = True
        print("You Win.")
    print(Hangman_art.stages[lives])