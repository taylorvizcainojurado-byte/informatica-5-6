import time
def main():

    x = 4
    password = "password:"
    ppp = input("Enter password:")

    if ppp == password:
        print("Success, Welcome to Diddy´s Dungeon! ")
        print("This program will genuinly\nchimi your changa in 5 seconds.")
        for i in range(4):
                    time.sleep(1)
                    print(x)
                    x = x - 1

    else:
        print("Incorrect\nThis program will genuinly\nchimi your changa in 5 seconds.")
        for i in range(4):
            time.sleep(1)
            print(x)
            x = x - 1

    print("Changa succesfully chimied.")










if __name__ == "__main__":
    main()
