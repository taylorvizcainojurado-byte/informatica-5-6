import random
def main():

    coin = ["heads","tails"]
    attempts = 3
    while attempts > 0:
        flip = random.choice(coin)
        ges = input("Heads or Tails: ").strip().lower()

        print("The coin landed on", flip)



        if ges == flip:
            print("You Win!")
            break
        else:
            print("You Lose!")
            attempts -= 1
            print("Attempts left:", attempts)


if __name__ == "__main__":
    main()
