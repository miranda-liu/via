import csv
import json

# Read data from CSV and convert it to JSON
csv_file = 'data/2023BostonCrime.csv'  # Replace with your CSV file name
json_data = {'type': 'FeatureCollection', 'features': []}

with open(csv_file, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        location = row['Location']
        if not location:
            continue
        latitude = float(row['Lat'])
        longitude = float(row['Long'])
        title = row['OFFENSE_DESCRIPTION']

        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [longitude, latitude]
            },
            'properties': {
                'title': title
            }
        }
        json_data['features'].append(feature)
json_string = json.dumps(json_data)
print(f'const jsonData = {json_string};')