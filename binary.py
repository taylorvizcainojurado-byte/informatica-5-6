def main():
    print("Binary to Decimal Converter ")
    print("The purpose of this program is to convert\nbinary numbers into normal numbers. ")

    def binary_to_decimal(a):
        a = [1,2,4,8,16,32,64,128]
        for i in a:
            a.append(str(i))
            total = i + a
            print(total)

    number = input("Enter a binary number: ")
    binary_to_decimal(number)
    a = [1,2,4,8,16,32,64,128]
    for i in a:
        a.append(str(i))
        print(a)








if __name__ == "__main__":
    main()
