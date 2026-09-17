def main():
    tasks = []
    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        new = input("Enter task: ").capitalize().strip()

        if new == "Exit":
            break

        if new not in tasks:
            tasks.append(new)
        elif new in tasks:
            tasks.remove(new)
            print("Task removed from the list. ")

if __name__ == "__main__":
    main()
