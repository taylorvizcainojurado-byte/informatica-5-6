def main():
    layer = input("Descent atmosphere layer: ").lower().strip()
    if layer == "exosphere":
        print("Your altitude level will be between 700–10,000 km")
    elif layer == "Exosphere":
        print("Your altitude level will be between 700–10,000 km")
    elif layer == "thermosphere":
        print("Your altitude level will be between 85–700 km")
    elif layer == "Thermosphere":
        print("Your altitude level will be between 85–700 km")
    elif layer == "mesosphere":
        print("Your altitude level will be between 50–85 km")
    elif layer == "Mesosphere":
        print("Your altitude level will be between 50–85 km")
    elif layer == "stratosphere":
        print("Your altitude level will be between 12–50 km")
    elif layer == "Stratosphere":
        print("Your altitude level will be between 12–50 km")
    elif layer == "Troposphere":
        print("Your altitude level will be between 0–12 km")
    elif layer == "troposphere":
        print("Your altitude level will be between 0–12 km")
    else:
        print("Invalid atmosphere layer")

    alt = float(input("Enter exact altitude: "))
    if alt < 10000 and alt >= 700:
        alt /= 2
        print(f"Total descent time: {alt} seconds")
    elif alt <= 699 and alt >= 85:
        alt /= 0.5
        print(f"Total descent time: {alt} seconds")
    elif alt <= 84 and alt >= 50:
        alt /= 0.2
        print(f"Total descent time: {alt} seconds")
    elif alt <= 49 and alt >= 12:
        alt /= 0.075
        print(f"Total descent time: {alt} seconds")
    elif alt <= 11 and alt >= 0:
        alt /= 0.02
        print(f"Total descent time: {alt} seconds")
    else:
        print("Invalid altitude")










if __name__ == "__main__":
    main()
