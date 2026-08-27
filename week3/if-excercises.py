def main():
    #easy
    number = int(input("Write a whole number: "))

    if number < 0:
        number *= -1
        print(number)

    #medium

    num1 = float(input("Write a number: "))
    num2 = float(input("Write another number: "))
    oper = input("Write a type of operation: ")

    if oper == "+":
        total = num1 + num2
        print(total)
    elif oper == "-":
        total2 = num1 - num2
        print(total2)
    elif oper == "*":
        total3 = num1 * num2
        print(total3)
    elif oper == "/":
        total4 = num1 / num2
        print(total4)
    else:
        print()

    #hard


    func = input("Write an arithmetic operation: ")

    parts = func.split(" ")
    numb1 = int(parts[0])
    operator = parts[1]
    numb2 = int(parts[2])

    if operator == "+":
        ttal = numb1 + numb2
        print(float(ttal))
    elif operator == "-":
        ttal2 = numb1 - numb2
        print(float(ttal2))
    elif operator == "*":
        ttal3 = numb1 * numb2
        print(float(ttal3))
    elif operator == "/":
        ttal4 = numb1 / numb2
        print(float(ttal4))












#pro tip
    arith = input("Write an arithmetic operation: ").strip()
    try:
        if "/ 0" in arith:
            print("Error: Cannot divide by zero")
        else:
            total = float(eval(arith))

            print(f"{total:.1f}")

    except:
        print("Invalid Format")








if __name__ == "__main__":
    main()

