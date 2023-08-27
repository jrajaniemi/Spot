import requests
import xmltodict
import json
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

def fetch_electricity_prices(start, end, area):
    # ENTSO-E API endpoint for market data
    url = "https://web-api.tp.entsoe.eu/api"

    # Parameters for the request
    params = {
        'securityToken': os.getenv('ENTSOE_API_KEY'),  # API key from .env file
        'documentType': 'A44',  # A44 is the document type for prices
        'in_Domain': area,  # The area for which you want to fetch prices
        'out_Domain': area,
        'periodStart': start,
        'periodEnd': end,
    }

    try:
        # Make the request
        response = requests.get(url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Convert XML response to JSON
            response_json = json.dumps(xmltodict.parse(response.text))
            # Save the JSON response to a file with a timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            with open(f'response_{timestamp}.json', 'w') as f:
                f.write(response_json)
            return response_json
        else:
            print("Error:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None

# Example usage:
start = '202308010000'
end = '202308080000'
area = '10YFI-1--------U'  # This is the EIC code for Finland

prices = fetch_electricity_prices(start, end, area)
print(prices)
