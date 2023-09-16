import csv
import offense_codes as offenses

def main():
    csv_name = 'data/2023BostonCrime.csv'
    with open(csv_name, 'r', newline = '') as file:
        bad_offenses = offenses.get_bad_offense_codes()
        reader = csv.reader(file)
        locations,  = {}
        for i, row in enumerate(reader):
            if i == 0:
                continue

            location = get_location(row[16])
            offense_code = int(row[1])
            if offense_code not in bad_offenses:
                continue
            crimes = locations.get(location,{})
            crimes[offense_code] = crimes.get(offense_code,0) + 1
            locations[location] = crimes
        print(locations)

def get_location(loc_string):
    # Some reports don't include locations
    if not loc_string:
        return ""
    coord = loc_string[1:-1].split(", ")
    location = round(float(coord[0]),6), round(float(coord[1]),6)
    return location