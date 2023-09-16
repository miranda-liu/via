import csv

csv_name = '2023BostonCrime.csv'
with open(csv_name, 'r', newline = '') as file:
    reader = csv.reader(file)
    offense_codes = {}
    for i,row in enumerate(reader):
        if not i:
            continue
        code, description = int(row[1]), row[3]
        if not description:
            continue
        if code not in offense_codes:
            offense_codes[code] = description
for k,v in offense_codes.items():
    print(k,v)
print(len(offense_codes))