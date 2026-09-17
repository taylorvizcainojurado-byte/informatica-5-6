def main():
    tasks = []

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add, complete, exit): ").strip().lower()
        if command == "add":
            new = input("Enter new task: ")
            tasks.insert(0,new)
        elif command == "complete":
            comp = input("Which task do I complete? ")
            tasks.remove(comp)
        elif command == "exit":
            print("See you later! ")
            break
        else:
            print("Invalid response")











if __name__ == "__main__":
    main()
