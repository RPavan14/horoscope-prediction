# Define a function to get the ordinal suffix
def get_ordinal_suffix(number):
    if 10 <= number % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
    return suffix

def calculateHouseLord(asc_sign):

    # Define a list of zodiac signs in order
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    # Input the ascendant sign
    ascendant_sign = asc_sign

    # Find the index of the ascendant sign in the zodiac_signs list
    ascendant_index = zodiac_signs.index(ascendant_sign)

    # Define the lords of zodiac signs
    zodiac_lords = {
        "Aries": "Mars",
        "Taurus": "Venus",
        "Gemini": "Mercury",
        "Cancer": "Moon",
        "Leo": "Sun",
        "Virgo": "Mercury",
        "Libra": "Venus",
        "Scorpio": "Mars",
        "Sagittarius": "Jupiter",
        "Capricorn": "Saturn",
        "Aquarius": "Saturn",
        "Pisces": "Jupiter"
    }

    return ascendant_index, zodiac_signs, zodiac_lords

def printHouseLords(ascendant_index, zodiac_signs, zodiac_lords, moon_nakshatra,sun_nakshatra,mercury_nakshatra,venus_nakshatra, mars_nakshatra, jupiter_nakshatra, saturn_nakshatra, rahu_nakshatra, ketu_nakshatra):
    # Iterate through the houses
    print("-------------------------------------")
    print("Your Houses and their Lords: ")
    print("-------------------------------------")
    for i in range(12):
        house_number = i + 1
        house_sign_index = (ascendant_index + i) % 12
        house_sign = zodiac_signs[house_sign_index]
        house_lord = zodiac_lords[house_sign]
        
        # Find the Nakshatra of the house lord
        if house_lord == "Sun":
            house_lord_nakshatra = sun_nakshatra
        elif house_lord == "Moon":
            house_lord_nakshatra = moon_nakshatra
        elif house_lord == "Mercury":
            house_lord_nakshatra = mercury_nakshatra
        elif house_lord == "Venus":
            house_lord_nakshatra = venus_nakshatra
        elif house_lord == "Mars":
            house_lord_nakshatra = mars_nakshatra
        elif house_lord == "Jupiter":
            house_lord_nakshatra = jupiter_nakshatra
        elif house_lord == "Saturn":
            house_lord_nakshatra = saturn_nakshatra
        elif house_lord == "Rahu":
            house_lord_nakshatra = rahu_nakshatra
        elif house_lord == "Ketu":
            house_lord_nakshatra = ketu_nakshatra
        else:
            house_lord_nakshatra = "Unknown"

        suffix = get_ordinal_suffix(house_number)
        print(f"{house_number}{suffix} Lord is in {house_lord_nakshatra} Nakshatra")
    print("-------------------------------------")
    print("\n\n\n")