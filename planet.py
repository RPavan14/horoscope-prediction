from importLibraries import *
import flatlib

#Start the program
startProgram()

#Fetch User Location
lat,long = getLocation() 

#Fetch User Birth Data
date = fetchBirthData()

#Construct and Calculate Birth Chart
moon,ascendant,sun,mercury,venus,jupiter,saturn,mars,rahu,ketu = construct_Chart(lat,long,date)

#Calculate all Nakshatras
moon_nakshatra = calculate_nakshatra(moon.lon)
asc_nakshatra = calculate_nakshatra(ascendant.lon)
sun_nakshatra = calculate_nakshatra(sun.lon)
mercury_nakshatra = calculate_nakshatra(mercury.lon)
venus_nakshatra = calculate_nakshatra(venus.lon)
mars_nakshatra = calculate_nakshatra(mars.lon)
jupiter_nakshatra = calculate_nakshatra(jupiter.lon)
saturn_nakshatra = calculate_nakshatra(saturn.lon)
rahu_nakshatra = calculate_nakshatra(rahu.lon)
ketu_nakshatra = calculate_nakshatra(ketu.lon)

# Calculate all zodiac signs
asc_sign = str(calculate_zodiac_sign(ascendant.lon))
sun_sign = str(calculate_zodiac_sign(sun.lon))
moon_sign = str(calculate_zodiac_sign(moon.lon))
mercury_sign = str(calculate_zodiac_sign(mercury.lon))
venus_sign = str(calculate_zodiac_sign(venus.lon))
mars_sign = str(calculate_zodiac_sign(mars.lon))
jupiter_sign = str(calculate_zodiac_sign(jupiter.lon))
saturn_sign = str(calculate_zodiac_sign(saturn.lon))
rahu_sign = str(calculate_zodiac_sign(rahu.lon))
ketu_sign = str(calculate_zodiac_sign(ketu.lon))

#Calculate House Lords
ascendant_index,zodiac_signs,zodiac_lords = calculateHouseLord(asc_sign)

#Print House Lords
printHouseLords(ascendant_index, zodiac_signs, zodiac_lords, moon_nakshatra,sun_nakshatra,mercury_nakshatra,venus_nakshatra, mars_nakshatra, jupiter_nakshatra, saturn_nakshatra, rahu_nakshatra, ketu_nakshatra)

#Print Planets and Their Signs
printPlanetsAndTheirSigns(asc_sign,sun_sign,moon_sign,mercury_sign,mars_sign,venus_sign,jupiter_sign,saturn_sign,rahu_sign,ketu_sign)

#print Planets and their Nakshatras
printPlanetsAndTheirNakshatras(asc_nakshatra, moon_nakshatra,sun_nakshatra,mercury_nakshatra,venus_nakshatra, mars_nakshatra, jupiter_nakshatra, saturn_nakshatra, rahu_nakshatra, ketu_nakshatra)

#Print Houses and their Signs
printHousesAndTheirSigns(ascendant_index, zodiac_signs)

print(ascendant.lon)


