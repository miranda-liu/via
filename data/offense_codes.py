import csv

csv_name = '2023BostonCrime.csv'
with open(csv_name, 'r', newline = '') as file:
    reader = csv.reader(file)
    offense_codes = {}
    for row in reader:
        code, description = row[1], row[3]
        if not description:
            continue
        if code not in offense_codes:
            offense_codes[code] = description