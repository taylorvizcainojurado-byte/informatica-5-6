def main():
    name = input("What is your name? ").strip().title()
    color = input("Pick a color: ").strip().lower()
    adjective = input("Give me an adjective: ").strip().lower()
    adjectives = input("Give me another adjective: ").strip().lower()
    slime = input("Give me a gross adjective: ").strip().lower()
    verb = input("Give me a verb: ").strip().lower()
    verbs = input("Give me a verb in the past: ").strip().lower()
    person = input("Name a person: ").strip().title()
    persons = input("Name a person you hate: ").strip().title()
    animal = input("Name an animal: ").strip().lower()
    goal = input("A goal you would like to achieve: ").strip().lower()


    # Formatted Strings
    print(f"")
    print(f"Hello {name}!")
    print(f"")
    print(f"This is your story: ")
    print(f"  At Uranus you are the color {color},\n and you are very {adjective}.\n You randomly decided you would {goal}.\n This made you feel {adjectives}.\nEven though you like to {verb}, {person} still loves you, even though you dont love them back.\nYou placed a restraining order on {person} because he {verbs} and you didnt like that.\nYou asked {persons} to help you out because you love {persons}.\nIn the end you found out that you are a {slime} person and youre proud of it. You identify as a {animal}.")
    print(f"")
    yell = f"At Uranus you are the color {color},\n and you are very {adjective}.\n You randomly decided you would {goal}.\n This made you feel {adjectives}.\nEven though you like to {verb}, {person} still loves you, even though you dont love them back.\nYou placed a restraining order on {person} because he {verbs} and you didnt like that.\nYou asked {persons} to help you out because you love {persons}.\nIn the end you found out that you are a {slime} person and youre proud of it. You identify as a {animal}."
    print(yell.upper())



if __name__ == "__main__":
    main()
