def main():
    valid = []
    for i in range(1,11):
        valid.append(str(i))
    print("Welcome to the Times Table Test! ")

    test = input("What table would you like to be tested on?: ").lower().strip()
    max = int(input("Enter maximum value for the times table: "))

    print(f"Here is the {test} times table test")

    for x in range(1,max+1):
        ans = x * int(test)
        bb = True

        while bb:
            try:
                answ = int(input(f"{x} times {test} is... "))
                bb = False
            except ValueError:
                print("Invalid ")
        if answ == ans:
            print("Correct! ")
        else:
            print("Incorrect ")



if __name__ == "__main__":
    main()
