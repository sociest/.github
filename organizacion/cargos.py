import requests
import yaml
from datetime import datetime

endpoint_url = "https://script.google.com/macros/s/AKfycbx2NVuQOoHnwQCJ0-hN97nRz5CZ2ewCf93fSJh83b2hyYOUo5ACFHJQOaOB_XvEeYRD/exec?apiKey=1dyUadvJEDg2hWu00XCEAvZUNYbc&type="

def fetch_directory(type):
    response = requests.get(endpoint_url + type)
    response.raise_for_status()
    return response.json()

def generate_listing():
    types = ['fundador', 'titular', 'honorario']
    listings = []

    for type in types:
        members = fetch_directory(type)
        for member in members:
            listings.append({
                'fulll': member['name'],
                'joindate': datetime.now().strftime('%Y-%m-%d'),
                'description': f"Email: {member['email']}, Teléfono: {member['phone']}, Organización: {member['organization']}",
                'categories': [type.capitalize()],
                'file': member['icon'] or "",
            })

    with open('organizacion/miembros/directory.yml', 'w') as file:
        yaml.dump(listings, file, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    try:
        generate_listing()
        print("Listing generated successfully.")
    except Exception as e:
        print(f"Error generating listing: {e}")