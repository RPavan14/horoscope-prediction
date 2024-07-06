def calculate_nakshatra(longitude):
    # Calculate Nakshatra based on the provided formula
    nakshatra_number = ((longitude * 60) / 800) 

    # Adjust for the case where the result is 27
    if nakshatra_number == 27:
        nakshatra_number = 0

    # Define a list of Nakshatras
    nakshatras = [
        "Ashwini", "Bharani", "Kritika", "Rohini", "Mrigashira", "Ardra",
        "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
        "Hasta", "Chitra", "Swati", "Vishakaha", "Anuradha", "Jyestha", "Moola",
        "Poorvaashada", "Uttraashada", "Sharavan", "Dhansita", "Shatbhisa",
        "Poorvabhadrapada", "Uttarbhadrapada", "Revati"
    ]

    # Return the Nakshatra based on the Nakshatra number
    return nakshatras[int(nakshatra_number)]
  

def printPlanetsAndTheirNakshatras(asc_nakshatra, moon_nakshatra,sun_nakshatra,mercury_nakshatra,venus_nakshatra, mars_nakshatra, jupiter_nakshatra, saturn_nakshatra, rahu_nakshatra, ketu_nakshatra ):
    print("-------------------------------------")
    print("Your Planets and their Nakshatras: ")
    print("-------------------------------------")
    print(" Ascendant is in ",asc_nakshatra, " Nakshatra")
    print(" Moon is in ",moon_nakshatra, " Nakshatra")
    print(" Sun is in ",sun_nakshatra, " Nakshatra")
    print(" Mercury is in ",mercury_nakshatra, " Nakshatra")
    print(" Venus is in ",venus_nakshatra, " Nakshatra")
    print(" Mars is in ",mars_nakshatra, " Nakshatra")
    print(" Jupiter is in ",jupiter_nakshatra, " Nakshatra")
    print(" Saturn is in ",saturn_nakshatra, " Nakshatra")
    print(" Rahu is in ",rahu_nakshatra, " Nakshatra")
    print(" Ketu is in ",ketu_nakshatra, " Nakshatra") 
    print("-------------------------------------")
    print("\n\n")