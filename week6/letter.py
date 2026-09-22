def main():
    mario = ["Mario", "Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser"]

    for receiver in mario:
        if receiver != "Princess Peach":
            print(f"""
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver},

    You are cordially invited to a ball at
    Peach's Castle this evening, 7:00 PM.

    Sincerely,
    {mario[5]}
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
                        """)










if __name__ == "__main__":
    main()
