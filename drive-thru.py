def main():
    def welcome():
        print("Welcome to Crazy Eyes!")
        menu = ["Cheeseburger","Fries","Soda", "Ice Cream", "Cookie"]
        print("Heres the menu: ")
        x = 0
        y = 1
        for i in menu:
            print(f"{y}. {menu[x]}")
            x += 1
            y += 1

    welcome()

    def get_item(a):
        try:
            if a == "cheeseburger":
                print("🍔")
            elif a == "fries":
                print("🍟")
            elif a == "soda":
                print("🥤")
            elif a == "ice cream":
                print("🍦")
            elif a == "cookie":
                print("🍪")
            else:
                print("We dont have that")
        except ValueError:
            print("Invalid Choice")

    choice = input("What would you like to order? ").lower().strip()
    print("Perfect!")
    get_item(choice)








if __name__ == "__main__":
    main()
