def main():
    not_validated = True
    while not_validated:
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number >= 10 and number <= 1:
                print("Between 1 and 10")
            else:
                not_validated = False
        except ValueError:
            print("You have to enter a NUMBER BETWEEN 1 AND 10: ")






if __name__ == "__main__":
    main()
