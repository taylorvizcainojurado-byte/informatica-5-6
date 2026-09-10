from datetime import datetime
def main():

    day = datetime.now().weekday()

    if day < 4:
        print("Its a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("Its Friday")
        print("Just a day left until the weekend")
    else:
        print("Its the weekend!")






if __name__ == "__main__":
    main()
