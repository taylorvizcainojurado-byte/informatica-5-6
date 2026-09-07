def main():
    answer = ""

    while answer != "Yes!":
        answer = input("Are we there yet? ").strip().title()
        if answer == "Yes":
            followup = input("Really? ").title().strip()
        if followup == "Yes":
            break
        else:
            print("I hate you gng ")
    print("We are here! ")




if __name__ == "__main__":
    main()
