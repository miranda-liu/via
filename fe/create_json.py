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

# Convert the JSON data to a string
json_string = json.dumps(json_data)

# Create the HTML file
html_code = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Add markers to a web map with a symbol layer</title>
    <meta name="viewport" content="initial-scale=1,maximum-scale=1,user-scalable=no">
    <link href="https://api.mapbox.com/mapbox-gl-js/v2.14.1/mapbox-gl.css" rel="stylesheet">
    <script src="https://api.mapbox.com/mapbox-gl-js/v2.14.1/mapbox-gl.js"></script>
    <style>
        body {{ margin: 0; padding: 0; }}
        #map {{ position: absolute; top: 0; bottom: 0; width: 100%; }}
    </style>
</head>
<body>
<div id="map"></div>
<script>
    mapboxgl.accessToken = 'pk.eyJ1Ijoicmt1YmEiLCJhIjoiY2xtbDZtbnBtMDg3MzJrbW9jNTJqMzVibiJ9.1G7FCXA5MdikERXLIAuJLQ';
    const map = new mapboxgl.Map({{
        container: 'map',
        // Choose from Mapbox's core styles, or make your own style with Mapbox Studio
        style: 'mapbox://styles/mapbox/streets-v12',
        center: [-96, 37.8],
        zoom: 3
    }});
    
    map.on('load', () => {{
        // Add an image to use as a custom marker
        map.loadImage(
            'https://docs.mapbox.com/mapbox-gl-js/assets/custom_marker.png',
            (error, image) => {{
                if (error) throw error;
                map.addImage('custom-marker', image);
                // Add a GeoJSON source with points from the CSV data
                const json = {json_string};
                map.addSource('points', {{
                    'type': 'geojson',
                    'data': json
                }});
                
                // Add a symbol layer
                map.addLayer({{
                    'id': 'points',
                    'type': 'symbol',
                    'source': 'points',
                    'layout': {{
                        'icon-image': 'custom-marker',
                        'text-field': ['get', 'title'],
                        'text-font': [
                            'Open Sans Semibold',
                            'Arial Unicode MS Bold'
                        ],
                        'text-offset': [0, 1.25],
                        'text-anchor': 'top'
                    }}
                }});
            }}
        );
    }});
</script>
</body>
</html>
"""

# Write the HTML code to an HTML file
with open('fe/map_with_markers.html', 'w') as html_file:
    html_file.write(html_code)
