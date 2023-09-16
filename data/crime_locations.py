import csv
import math

csv_name = '2023BostonCrime.csv'
with open(csv_name, 'r', newline = '') as file:
    reader = csv.reader(file)
    locations = {}
    for i, row in enumerate(reader):
        if i == 0:
            continue
        location, offense_code = row[16], int(row[1])
        if not location:
            continue
        coord = location[1:-1].split(", ")
        location = round(float(coord[0]),5), round(float(coord[1]),5)
        crimes = locations.get(location,{})
        crimes[offense_code] = crimes.get(offense_code,0) + 1
        locations[location] = crimes
    print(locations)
