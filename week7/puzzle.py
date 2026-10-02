def main():
    validated = True
    while validated:
        try:
            number = int(input("Enter a number: "))
            validated = False
        except ValueError:
            print("You must enter a NUMBER: ")



if __name__ == "__main__":
    main()
