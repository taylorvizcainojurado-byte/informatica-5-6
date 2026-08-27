def main():

    spain = int(input("Spain Goals: "))
    argentina = int(input("Argentina Goals: "))
    if spain > argentina:
        print("Spain cooked Argentina´s goose.")
    elif argentina > spain:
        print("Argentina sadly won")
    else:
        print("Tie: Both are trash.")



if __name__ == "__main__":
    main()
