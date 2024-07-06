from flatlib.datetime import Datetime

def fetchBirthData():
    date_input = str(input("Enter Date in format YYYY/MM/DD: \n"))
    time_input = str(input("Enter Time in format HH:MM: \n"))
    date = Datetime(str(date_input), str(time_input), '+05:30')
    return date
