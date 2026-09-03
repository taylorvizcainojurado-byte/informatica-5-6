import random

def main():
    name = input("Hello! What is your name? ").title().strip()

    number = random.randint(1,100)
    print(f"Well, {name}, I am thinking of a number between 1 and 100 ")
    guess1 = int(input("Take a guess! "))

    att = 0
    while att < 5:
        if guess1 < number:
            print("Your guess is too low")
            guess1 = int(input("Take a guess! "))
            att += 1
        elif guess1 > number:
            print("Your guess is too high")
            guess1 = int(input("Take a guess! "))
            att += 1
        elif guess1 == number:
            print(f"Correct! Good job {name} you guessed my number! ")
            break
        else:
            print("Invalid guess")
            guess1 = int(input("Take a guess! "))
            att += 1




if __name__ == "__main__":
    main()
