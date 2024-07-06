def printHousesAndTheirSigns(ascendant_index, zodiac_signs):
    # Calculate and print the houses
    print("-------------------------------------")
    print("Your Houses and Signs: ")
    print("-------------------------------------")
    for i in range(12):
        house_number = i + 1
        house_sign_index = (ascendant_index + i) % 12
        house_sign = zodiac_signs[house_sign_index]
        print(f"House {house_number} is in {house_sign} Sign")
    print("-------------------------------------")
    print("\n\n")