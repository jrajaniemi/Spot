# SPOT.PY

This Python script fetches electricity market data, specifically the prices, from the ENTSO-E's Transparency Platform API. The code utilizes `requests` to send a GET request to the API, `dotenv` for environment variables management, and `xmltodict` for parsing the API's XML response to JSON.

## Requirements

Ensure you have the following dependencies installed on your machine:

- Python 3.6+
- python-dotenv
- requests
- xmltodict
- json

You can install these packages using pip:

```bash
pip install python-dotenv requests xmltodict
```

## Setup

1. Clone this repository to your local machine.

```bash
git clone https://github.com/jrajaniemi/Spot
```

2. Navigate to the directory.

```bash
cd Spot
```
3. Create a `.env` file in the same directory to store your ENTSO-E's Transparency Platform API key like so:

```bash
ENTSOE_API_KEY=your_api_key
```
Replace `your_api_key` with your actual API key.

## Usage

1. The script can be run using the following command:

```bash
python spot.py
```

This script fetches market data for a given time period (a year back from the current date by default) for a specified region (Finland in the example). It then extracts the relevant information from the JSON response, removes unwanted data, and saves the filtered data to a JSON file. In case of a failure, it prints the corresponding error message.

The area for which you want to fetch data should be provided as an EIC code. For example, the EIC code for Finland is '10YFI-1--------U'. To fetch data for a different area, replace this value with the respective EIC code.
