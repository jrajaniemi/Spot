
# spot.py

## Overview
`spot.py` is a Python script that fetches electricity prices from the ENTSO-E (European Network of Transmission System Operators for Electricity) API and saves the response in a JSON file.

## Functionality
1. Imports necessary libraries such as `requests`, `xmltodict`, `json`, `os`, and `dotenv`.
2. Loads environment variables from a `.env` file, which should contain the `ENTSOE_API_KEY`.
3. Defines a function `fetch_electricity_prices(start, end, area)` that fetches electricity prices for a specified area and time period.
    - `start`: The start time of the period for which you want to fetch prices (format: 'yyyyMMddHHmm').
    - `end`: The end time of the period for which you want to fetch prices (format: 'yyyyMMddHHmm').
    - `area`: The EIC (Energy Identification Code) of the area for which you want to fetch prices.
4. Sends a GET request to the ENTSO-E API with the specified parameters and API key.
5. If the request is successful, converts the XML response to JSON and saves it to a file with a timestamp. Otherwise, prints an error message.

## Installation
1. Make sure you have Python 3 installed on your machine.
2. Clone the repository or download the `spot.py` script.
3. Install the required packages by running `pip install -r requirements.txt` in the terminal.

## Usage
1. Create a `.env` file in the same directory as `spot.py` and add your ENTSO-E API key as `ENTSOE_API_KEY=your_api_key`.
2. Modify the `start`, `end`, and `area` variables in the `spot.py` script to the desired values.
3. Run the script by executing `python spot.py` in the terminal.

## Example
```python
# Example usage:
start = '202308010000'
end = '202308080000'
area = '10YFI-1--------U'  # This is the EIC code for Finland

prices = fetch_electricity_prices(start, end, area)
print(prices)
```
