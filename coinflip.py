import random

ges = int(input("Heads(1) or Tails(2): "))

otcm = random.randint(1,2)

if otcm == 1:
    print("Heads")
elif otcm == 2:
    print("Tails")
else:
    print("Not an Option")

if ges == otcm:
    print("You Win!")
else:
    print("You Lose!")


