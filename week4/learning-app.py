import random
import time

def main():


    print("Welcome to Math Daddy! ")
    ready = input("Are you ready to learn? ").lower().strip()
    if ready == "yes":
        print("Lets do this! ")
    elif ready == "no":
        print("Too bad bruh ")
    else:
        print("I dont really care ")
    streak = 0
    while streak < 3:
        math1 = random.randint(10,99)
        math2 = random.randint(10,99)
        operation = int(input(f"What is {math1} + {math2}? "))
        print(f"Your answer was {operation} ")
        total = math1 + math2

        if operation == total:
            print("Correct! ")
            streak += 1
            star = "⭐" * streak
            print(f"Streak: {star} ")

        else:
            streak = 0
            print("Incorrect")
            print(f"The correct answer is {total} ")










if __name__ == "__main__":
    main()
