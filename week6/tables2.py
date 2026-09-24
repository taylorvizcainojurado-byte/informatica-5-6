def main():
    while True:
        table = input("Enter a number: ").lower().strip()
        if table == "exit":
            break
        else:

            max = int(input("Enter maximum value for the times table: "))

            print(f"Here is the {table} times table")

            for x in range(1,max+1):
                ans = x * int(table)
                print(f"{x} times {table} is {ans}")


if __name__ == "__main__":
    main()

