#define main()
#   print(welcome)
#   pull possible words from a list using a random assign to a variable
#define hangman()
#   print how many letters we are using using len
#   assign a variable as lifecount = 5
#   input so the user can start using letters in a for loop
#   the person can only get 5 letters wrong
#   for each one wrong it has to print(lifecount - 1)
#   once the word is guessed print(you win)
#
#   hangman()
import random
def main():



    def start_game():
        with open("random_words.txt") as words:
            content = words.read().splitlines()
            word = random.choice(content)
            print("This is your word: ")
            line = ["_"]* len(word)
            print(" ".join(line))
        while True:
            guess = input("Take a guess: ")

            if len(guess) == 1:
                break
            else:
                print("Invalid Guess. Try Again ")

    start_game()


if __name__ == "__main__":
    main()
