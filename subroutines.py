def main():

    def calculate(a, b):
        answer = a + b
        print(f"{a} + {b} = {answer}")

    num1 = 10
    num2 = 15

    calculate(num1,num2)


    def average_value(a,b,c):
        answer = (a + b + c)/3
        print(f"The average value is {round(answer,1)}")

    average_value(6,8,10)

    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    z = float(input("Enter a third number: "))

    average_value(x,y,z)

if __name__ == "__main__":
    main()
