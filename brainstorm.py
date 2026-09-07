import random
import time

def main():
    ideas = ["Cutural Backround", "Lessons from failure", "Personal Challenges", "Debates on tecnology", "Education System", "Historical turning points", "Psychology concepts", "Literature", "Historical Speeches"]
    print("Cant think of ideas for your essay? ")
    help = input("Do you need help? ").lower().strip()
    if help == "yes":
        print("Okay I got your back! ")
    else:
        print("Im gonna help you anyway ")
    rndm = random.choice(ideas)
    print("Heres an idea that might help you out ")
    print(rndm)
    help2 = input("Does this help? ").lower().strip()
    while help2 != "yes":
        if help2 == "yes":
            print("Glad I could help! ")
            break
        else:
            print("Heres another idea ")
            print(rndm)











if __name__ == "__main__":
    main()
