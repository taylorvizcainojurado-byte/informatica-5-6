def main():
    with open("sample.txt") as new_file:
        content = new_file.read()
        print(content)

    count = 0
    with open("sample.txt") as hoco_week:
        for line in hoco_week:
            line = line.replace("\n","")
            count += 1
            print(f"Day {count}: {line}")

    #assignment
    def largest():
        number_list = []
        with open("random_numbers.txt") as number_list:
            for number in number_list:
                number = number.replace("\n","")
                number_list.append(int(number))
        print(max(number_list))

    largest()


if __name__ == "__main__":
    main()
