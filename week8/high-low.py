def main():
    def highest(a,b):
        if a < b:
            highest_num = b
            print(f"The highest number is {highest_num} ")
        elif a > b:
            highest_num = a
            print(f"The highest number is {highest_num} ")
        else:
            print("The numbers are the same")
    highest(8,2)

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    highest(num1,num2)

    def lowest(a,b,c):
        if a < b and a < c:
            lowest_num = a
            print(f"The lowest number is {lowest_num} ")
        elif b < a and b < c:
            lowest_num = b
            print(f"The lowest number is {lowest_num} ")
        elif c < a and c < b:
            lowest_num = c
            print(f"The lowest number is {lowest_num} ")
        else:
            print("The numbers are the same ")

    numb1 = int(input("Enter a number: "))
    numb2 = int(input("Enter a second number: "))
    numb3 = int(input("Enter a third number: "))

    lowest(numb1,numb2,numb3)











if __name__ == "__main__":
    main()
