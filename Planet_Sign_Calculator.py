def calculate_zodiac_sign(longitude):
    # Define the 12 zodiac signs and their corresponding degree ranges
    zodiac_signs = [
        ("Aries", (0, 30)),
        ("Taurus", (30, 60)),
        ("Gemini", (60, 90)),
        ("Cancer", (90, 120)),
        ("Leo", (120, 150)),
        ("Virgo", (150, 180)),
        ("Libra", (180, 210)),
        ("Scorpio", (210, 240)),
        ("Sagittarius", (240, 270)),
        ("Capricorn", (270, 300)),
        ("Aquarius", (300, 330)),
        ("Pisces", (330, 360))
    ]

    # Loop through the zodiac signs to find the one that matches the longitude
    for sign, (start, end) in zodiac_signs:
        if start <= longitude < end:
            return sign

    # Handle the case when longitude is exactly 360 degrees
    if longitude == 360:
        return "Aries"  # Considered as the first sign

    return "Invalid"  # Handle invalid input



def printPlanetsAndTheirSigns(asc_sign,sun_sign,moon_sign,mercury_sign,mars_sign,venus_sign,jupiter_sign,saturn_sign,rahu_sign,ketu_sign):
    print("\n\n")
    print("-------------------------------------")
    print("Your Planets and their Signs: ")
    print("-------------------------------------")
    print("Ascendant is in",asc_sign+ " Sign")
    print("Sun is in",sun_sign+ " Sign")
    print("Moon is in",moon_sign+ " Sign")
    print("Mercury is in",mercury_sign+ " Sign")
    print("Mars is in",mars_sign+ " Sign")
    print("Venus is in",venus_sign+ " Sign")
    print("Jupiter is in",jupiter_sign+ " Sign")
    print("Saturn is in",saturn_sign+ " Sign")
    print("Rahu is in",rahu_sign+ " Sign")
    print("Ketu is in",ketu_sign+ " Sign")
    print("-------------------------------------")
    print("\n\n")