def main():
    print("Binary to Decimal Converter ")
    print("The purpose of this program is to convert\nbinary numbers into normal numbers. ")

    def binary_to_decimal(a):
        a = []
        numbers = [1,2,4,8,16,32,64,128]
        for i in range(len(numbers)):
            total = a * 2 + a
            print(total)

    binary = list(input("Enter a binary number: "))
    binary_to_decimal(binary)







if __name__ == "__main__":
    main()
