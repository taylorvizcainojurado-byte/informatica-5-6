def main():
    num = int(input("Pick a number from 1-10 "))
    if num <= 10 and num >= 1:
        print("Okay perfect ")
    else:
        print("Invalid Option")
        num = int(input("Pls try again "))
        if num <= 10 and num >= 1:
                print("Okay perfect ")
        else:
            print("Invalid Option")
            num = int(input("Pls try again "))
            if num <= 10 and num >= 1:
                print("Okay perfect ")
            else:
                print("Invalid Option")
                num = int(input("Pls try again "))

    for i in range(10):
        if num<1 or num>10:
            print("Table not available ")

        else:
            i += 1
            z = i * num
            print(f"{i} times {num} is equal to {z} ")

    x = input("Want another table or exit ").strip().lower()


    while x or num1 != "exit":
        num1 = input("Pick another number or exit ")
        if num1 == "exit":
            print("Okay Bye!")
            break
        else:
            num2 = int(input("Which number do you want? "))


        for i in range(10):
            if num2<1 or num2>10:
                print("Table not available ")

            else:
                i += 1
                z = i * num2
                print(f"{i} times {num2} is equal to {z} ")












if __name__ == "__main__":
    main()
