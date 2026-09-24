def main():
    valid = []
    for i in range(1,11):
        valid.append(str(i))
    while True:
        table = input("Enter a number (1-10 or exit): ").lower().strip()
        if table == "exit":
            break
        else:

            max = int(input("Enter maximum value for the times table: "))

            print(f"Here is the {table} times table")

            for x in range(1,max+1):
                ans = x * int(table)
                print(f"{x} times {table} is {ans}")
            else:
                print("Invalid command")



if __name__ == "__main__":
    main()

