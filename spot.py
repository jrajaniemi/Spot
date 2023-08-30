import requests
import xmltodict
import json
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


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
            
            # Load the JSON response as a dictionary
            response_dict = json.loads(response_json)
            
            # Extract the TimeSeries array and its Period object
            time_series = response_dict['Publication_MarketDocument']['TimeSeries']
            for series in time_series:
                series.pop('mRID', None)
                series.pop('businessType', None)
                series.pop('in_Domain.mRID', None)
                series.pop('out_Domain.mRID', None)
                series.pop('currency_Unit.name', None)
                series.pop('price_Measure_Unit.name', None)
                series.pop('curveType', None)
            
            # Save the filtered JSON response to a file with a timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M")
            with open(f'response_{timestamp}.json', 'w') as f:
                f.write(json.dumps(time_series, separators=(',', ':')))
            return json.dumps(time_series, separators=(',', ':'))
        else:
            print("Error:", response.status_code, response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None

# Get the current date and time
now = datetime.now()

# Calculate the date of the day before the current date
end_date = now - timedelta(days=1)

# Set the time to the start of the day
end_date = end_date.replace(hour=0, minute=0, second=0)

# Format the end date and time as a string
end = end_date.strftime("%Y%m%d%H%M")

# Calculate the start date as 365 days before the end date
start_date = end_date - timedelta(days=365)

# Format the start date and time as a string
start = start_date.strftime("%Y%m%d%H%M")

# Example usage:
area = '10YFI-1--------U'  # This is the EIC code for Finland

# Example usage:
area = '10YFI-1--------U'  # This is the EIC code for Finland


prices = fetch_electricity_prices(start, end, area)
# print(prices)
