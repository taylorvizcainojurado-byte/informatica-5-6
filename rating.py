def main():

    print("Thanks for dining at Chatahoochee!")

    rating = float(input("Rate us on a scale from 1-5: "))

    if rating > 4.5:
        print("Absolutely Amazing!")

    elif rating > 3.5:
        print("Excellent Chatahoochee")

    elif rating > 2.5:
        print("Decently Good")
    elif rating > 1.5:
        print("Kinda Bad")
    else:
        print("Absolute Buns")
    print("Come again soon!")

if __name__ == "__main__":
    main()






