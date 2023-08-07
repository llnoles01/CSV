import csv
import matplotlib.pyplot as plt

from datetime import datetime

infile = open("sitka_weather_2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    if column_header == "TMIN":
        tmin_i = index
    elif column_header == "TMAX":
        tmax_i = index
    elif column_header == "DATE":
        date_i = index
    elif column_header == "NAME":
        name_i = index

highs = []
lows = []
dates = []

mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")

for row in csvfile:
    try:
        name1 = row[name_i]
        high = int(row[tmax_i])
        low = int(row[tmin_i])
        some_date = datetime.strptime(row[date_i], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {some_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(some_date)


fig = plt.figure()



fig.autofmt_xdate()

infile = open("death_valley_2018_simple.csv", "r")
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):
    if column_header == "TMIN":
        tmin_i = index
    elif column_header == "TMAX":
        tmax_i = index
    elif column_header == "DATE":
        date_i = index
    elif column_header == "NAME":
        name_i = index

highs = []
lows = []
dates = []

mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")

for row in csvfile:
    try:
        name2 = row[name_i]
        high = int(row[tmax_i])
        low = int(row[tmin_i])
        some_date = datetime.strptime(row[date_i], "%Y-%m-%d")
    except ValueError:
        print(f"Missing data for {some_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(some_date)

plt.subplot(2, 1, 1)

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, color="blue", alpha=0.1)

plt.title(name1, fontsize=12)
plt.xlabel("")

plt.tick_params(axis="both", which="major", labelsize=12)

plt.subplot(2, 1, 2)

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, color="blue", alpha=0.1)

plt.title(name2, fontsize=12)
plt.xlabel("")

plt.tick_params(axis="both", which="major", labelsize=12)

fig.autofmt_xdate()

plt.suptitle(f"Temperature comparison between {name1} and {name2}")

plt.show()