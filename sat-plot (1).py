import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_dates(num_dates, celestial_body):
    dates = []
    for i in range(1, num_dates + 1):
        date_str = input(f"Enter {celestial_body} date {i} (YYYY-MM-DD): ")
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        dates.append(date_obj)
    return dates

def calculate_date_ranges(dates, years, months):
    date_ranges = []
    for date in dates:
        new_date = date + datetime.timedelta(days=(years*365) + (months*30))
        date_ranges.append((date, new_date))
    return date_ranges

def plot_ranges(saturn_date_ranges):
    fig, ax = plt.subplots()

    for i, (start, end) in enumerate(saturn_date_ranges):
        ax.barh(f"Saturn {i+1}", (end - start).days, left=start, height=0.4, color='blue', alpha=0.7)
     
    ax.set_xlabel('Date')
    ax.set_ylabel('Celestial Bodies')
    ax.set_title('Saturn Date Ranges')

    # Format x-axis as dates
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    ax.legend()

    plt.show()

# Get Saturn dates
num_saturn_dates = int(input("Enter the number of Saturn dates: "))
saturn_dates = get_dates(num_saturn_dates, "Saturn")
saturn_date_ranges = calculate_date_ranges(saturn_dates, 2, 6)

# Plotting
plot_ranges(saturn_date_ranges)
