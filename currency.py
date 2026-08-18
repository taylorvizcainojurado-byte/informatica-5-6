def main():
    colombia = float(input("Amount of Colombian Pesos: "))
    peru = float(input("Amount of Peruvian Soles: "))
    brazil = float(input("Amount of Brazilian Reais: "))

    mxcol = colombia*0.0054
    uscol = colombia*0.00032

    mxper = peru*5.07
    usper = peru*0.30

    mxbra = brazil*3.27
    usbra = brazil*0.19

    totalmx = mxcol + mxper + mxbra
    totalus = uscol + usper + usbra

    mxred = round(totalmx,2)
    usred = round(totalus,2)

    print(f"USD: {usred}")
    print(f"MXP: {mxred}")


if __name__ == "__main__":
    main()
