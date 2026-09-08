import random


def main():
    ideas = ["Cutural Backround", "Lessons from failure", "Personal Challenges", "Debates on tecnology", "Education System", "Historical turning points", "Psychology concepts", "Literature", "Historical Speeches"]
    rndm = random.choice(ideas)
    print("Cant think of ideas for your essay? ")
    help = input("Do you need help? ").lower().strip()
    if help == "yes":
        print("Okay I got your back! ")
    else:
        print("Im gonna help you anyway ")

    print("Heres an idea that might help you out ")
    print(rndm)
    help2 = input("Does this help? ").lower().strip()
    while help2 != "yes":
        help3 = input("Want another idea? ").lower().strip()
        if help3 == "yes":
            print("Heres another idea! ")
            print(rndm)

        else:
            print("Glad I could Help! ")
            break











if __name__ == "__main__":
    main()
