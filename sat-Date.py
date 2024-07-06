import pandas as pd

def convert_degrees_to_sign(degrees):
    if 0 <= degrees < 30:
        return "Aries"
    elif 30 <= degrees < 60:
        return "Taurus"
    elif 60 <= degrees < 90:
        return "Gemini"
    elif 90 <= degrees < 120:
        return "Cancer"
    elif 120 <= degrees < 150:
        return "Leo"
    elif 150 <= degrees < 180:
        return "Virgo"
    elif 180 <= degrees < 210:
        return "Libra"
    elif 210 <= degrees < 240:
        return "Scorpio"
    elif 240 <= degrees < 270:
        return "Sagittarius"
    elif 270 <= degrees < 300:
        return "Capricorn"
    elif 300 <= degrees < 330:
        return "Aquarius"
    else:
        return "Pisces"

def check_aspect_saturn(planet_sign, other_sign):
    # Rules for aspect based on non-retrograde Saturn
    if not is_saturn_retrograde:
        aspects = {
            "Aries": ["Aries", "Gemini", "Libra", "Capricorn"],
            "Taurus": ["Taurus", "Cancer", "Scorpio", "Aquarius"],
            "Gemini": ["Gemini", "Leo", "Sagittarius", "Pisces"],
            "Cancer": ["Cancer", "Virgo", "Capricorn", "Aries"],
            "Leo": ["Leo", "Libra", "Aquarius", "Taurus"],
            "Virgo": ["Virgo", "Scorpio", "Pisces", "Gemini"],
            "Libra": ["Libra", "Sagittarius", "Aries", "Cancer"],
            "Scorpio": ["Scorpio", "Capricorn", "Taurus", "Leo"],
            "Sagittarius": ["Sagittarius", "Aquarius", "Gemini", "Virgo"],
            "Capricorn": ["Capricorn", "Pisces", "Cancer", "Libra"],
            "Aquarius": ["Aquarius", "Aries", "Leo", "Scorpio"],
            "Pisces": ["Pisces", "Taurus", "Virgo", "Sagittarius"],
        }
        return other_sign in aspects[planet_sign]
    else:
        # Rules for aspect based on retrograde Saturn
        aspects_retrograde = {
            "Aries": ["Aries", "Aquarius", "Libra", "Cancer"],
            "Taurus": ["Taurus", "Pisces", "Scorpio", "Leo"],
            "Gemini": ["Gemini", "Aries", "Sagittarius", "Virgo"],
            "Cancer": ["Cancer", "Taurus", "Capricorn", "Libra"],
            "Leo": ["Leo", "Gemini", "Aquarius", "Scorpio"],
            "Virgo": ["Virgo", "Cancer", "Pisces", "Sagittarius"],
            "Libra": ["Libra", "Leo", "Aries", "Capricorn"],
            "Scorpio": ["Scorpio", "Virgo", "Taurus", "Aquarius"],
            "Sagittarius": ["Sagittarius", "Libra", "Gemini", "Pisces"],
            "Capricorn": ["Capricorn", "Scorpio", "Cancer", "Aries"],
            "Aquarius": ["Aquarius", "Sagittarius", "Leo", "Taurus"],
            "Pisces": ["Pisces", "Capricorn", "Virgo", "Gemini"],
        }
        return other_sign in aspects_retrograde[planet_sign]

# Read the Excel file
df = pd.read_excel("C:\\Users\\R Pavan Kumar\\OneDrive\\Desktop\\LahiriOnly.xlsx")


# User inputs
lagna_sign = input("Enter Lagna Sign: ")
lagna_lord_sign = input("Enter Lagna Lord Sign: ")
seventh_house_sign = input("Enter 7th House Sign: ")
seventh_lord_sign = input("Enter 7th Lord Sign: ")
# User input for Lagna Lord and 7th Lord
lagna_lord = input("Enter Lagna Lord: ")
seventh_lord = input("Enter 7th Lord: ")

# Assume you have a column "IsSatRetro" in your DataFrame
is_saturn_retrograde = df["isSatRetro"].iloc[0]  # Assuming the retrograde status is the same for all rows

# Apply the rules to create new columns
df["IsSaturnAspectingLagnaSign"] = df["Saturn"].apply(lambda x: check_aspect_saturn(convert_degrees_to_sign(x), lagna_sign))
df["IsSaturnAspectingLagnaLordSign"] = df["Saturn"].apply(lambda x: check_aspect_saturn(convert_degrees_to_sign(x), lagna_lord_sign))
df["IsSaturnAspecting7thHouseSign"] = df["Saturn"].apply(lambda x: check_aspect_saturn(convert_degrees_to_sign(x), seventh_house_sign))
df["IsSaturnAspecting7thLordSign"] = df["Saturn"].apply(lambda x: check_aspect_saturn(convert_degrees_to_sign(x), seventh_lord_sign))

# Save the new DataFrame to a new Excel file
#df.to_excel("Modified_LahiriOnly.xlsx", index=False)


#### NEW FILE

import pandas as pd

# Function to convert degrees to sign
def degrees_to_sign(degrees):
    if 0 <= degrees < 30:
        return "Aries"
    elif 30 <= degrees < 60:
        return "Taurus"
    elif 60 <= degrees < 90:
        return "Gemini"
    elif 90 <= degrees < 120:
        return "Cancer"
    elif 120 <= degrees < 150:
        return "Leo"
    elif 150 <= degrees < 180:
        return "Virgo"
    elif 180 <= degrees < 210:
        return "Libra"
    elif 210 <= degrees < 240:
        return "Scorpio"
    elif 240 <= degrees < 270:
        return "Sagittarius"
    elif 270 <= degrees < 300:
        return "Capricorn"
    elif 300 <= degrees < 330:
        return "Aquarius"
    else:
        return "Pisces"

# Function to check aspect based on retrograde status
def check_aspect_saturn(saturn_sign, other_sign, is_retrograde):
    if not is_retrograde:
        return saturn_sign == other_sign
    else:
        return (
            (saturn_sign == other_sign) or
            ((saturn_sign == "Aries" and other_sign in ["Aries", "Aquarius", "Libra", "Cancer"]) or
             (saturn_sign == "Taurus" and other_sign in ["Taurus", "Pisces", "Scorpio", "Leo"]) or
             (saturn_sign == "Gemini" and other_sign in ["Gemini", "Aries", "Sagittarius", "Virgo"]) or
             (saturn_sign == "Cancer" and other_sign in ["Cancer", "Taurus", "Capricorn", "Libra"]) or
             (saturn_sign == "Leo" and other_sign in ["Leo", "Gemini", "Aquarius", "Scorpio"]) or
             (saturn_sign == "Virgo" and other_sign in ["Virgo", "Cancer", "Pisces", "Sagittarius"]) or
             (saturn_sign == "Libra" and other_sign in ["Libra", "Leo", "Aries", "Capricorn"]) or
             (saturn_sign == "Scorpio" and other_sign in ["Scorpio", "Virgo", "Taurus", "Aquarius"]) or
             (saturn_sign == "Sagittarius" and other_sign in ["Sagittarius", "Libra", "Gemini", "Pisces"]) or
             (saturn_sign == "Capricorn" and other_sign in ["Capricorn", "Scorpio", "Cancer", "Aries"]) or
             (saturn_sign == "Aquarius" and other_sign in ["Aquarius", "Sagittarius", "Leo", "Taurus"]) or
             (saturn_sign == "Pisces" and other_sign in ["Pisces", "Capricorn", "Virgo", "Gemini"]))
        )

# Function to create new columns
def create_aspect_columns_saturn(df, lagna_lord, seventh_lord):
    for index, row in df.iterrows():
        saturn_sign = degrees_to_sign(row["Saturn"])
        lagna_lord_aspect = check_aspect_saturn(saturn_sign, degrees_to_sign(row[lagna_lord]), not row["isSatRetro"])
        seventh_lord_aspect = check_aspect_saturn(saturn_sign, degrees_to_sign(row[seventh_lord]), not row["isSatRetro"])
        df.at[index, "IsSaturnAspectingLagnaLord"] = lagna_lord_aspect
        df.at[index, "IsSaturnAspecting7thLord"] = seventh_lord_aspect

# Load your dataframe here, replace 'your_dataframe.csv' with the actual file path



# Create new columns
create_aspect_columns_saturn(df, lagna_lord, seventh_lord)

# Save the new dataframe to a new file
#df.to_excel('output_dataframe.xlsx', index=False)

###NEW FILE

import pandas as pd
df['LagnaAspect'] = df[['IsSaturnAspectingLagnaSign', 'IsSaturnAspectingLagnaLordSign', 'IsSaturnAspectingLagnaLord']].any(axis=1)
df['7thAspect'] = df[['IsSaturnAspecting7thHouseSign', 'IsSaturnAspecting7thLordSign', 'IsSaturnAspecting7thLord']].any(axis=1)
#df['BothTrue'] = df[['LagnaAspect','7thAspect']]
df['LSign'] = df['IsSaturnAspectingLagnaSign']
df['LLSign'] = df['IsSaturnAspectingLagnaLordSign']
df['LL'] = df['IsSaturnAspectingLagnaLord']
df['7Sign'] = df['IsSaturnAspecting7thHouseSign']
df['7LSign'] = df['IsSaturnAspecting7thLordSign']
df['7L'] = df['IsSaturnAspecting7thLord']

filtered2_df = df[(df['LagnaAspect'] == True) & (df['7thAspect'] == True)]

# Read the Excel file
#file_path = "LahiriOnly_v4.0.xlsx"
data = filtered2_df

# Extract the required columns (date and last 6 columns)
date_column = data.iloc[:, 1]  # Second column as date column
boolean_columns = data.iloc[:, -6:]  # Last 6 columns containing boolean values

# Create a new column counting the number of "TRUE" values in the last 6 columns
data['Count_TRUE'] = boolean_columns.apply(lambda row: row.tolist().count(True), axis=1)

# Ask user for date of birth
dob_input = input("Please enter your date of birth (dd/mm/yyyy): ")
user_dob = pd.to_datetime(dob_input, format='%d/%m/%Y')

# Calculate when the user will turn 21 and 35
date_21_years_old = user_dob + pd.DateOffset(years=21)
date_35_years_old = user_dob + pd.DateOffset(years=35)

# Filter the data based on the user's turning 21 and 35 dates
filtered_data = data[(date_column >= date_21_years_old) & (date_column <= date_35_years_old)]

# Get the max value of the 'Count_TRUE' column in the filtered data
max_count_true = filtered_data['Count_TRUE'].max()

# Further filter the data based on the max value in 'Count_TRUE'
max_count_true_data = filtered_data[filtered_data['Count_TRUE'] == max_count_true]

# Function to filter dates as per the specified conditions
def filter_dates(data):
    result = []
    prev_date = None
    for index, row in data.iterrows():
        current_date = row.iloc[1]  # Assuming the date column is in the second position
        if prev_date is None or (current_date.day != prev_date.day and current_date.month != prev_date.month):
            result.append(current_date)
        prev_date = current_date
    return result

# Apply the date filtering function
final_dates = filter_dates(max_count_true_data)

# Output the remaining dates after applying the specified conditions
print("Remaining dates after filtering:")
for date in final_dates:
    print(date)

### new
from datetime import datetime, timedelta

def filter_dates(original_dates):
    filtered_dates = [original_dates[0]]  # Start with the first date

    for i in range(1, len(original_dates)):
        current_date = original_dates[i]
        previous_date = pd.to_datetime(filtered_dates[-1])

        # Check if the current date is either the very next date or has the same or next month
        if current_date == previous_date + timedelta(days=1) or (
            current_date.month == previous_date.month
        ) :
            continue
        else:
            filtered_dates.append(original_dates[i])

    return filtered_dates


filtered_dates = filter_dates(final_dates)
print("Ye le")

print(filtered_dates)

for timestamp in filtered_dates:
    print(timestamp.strftime('%Y-%m-%d'))
