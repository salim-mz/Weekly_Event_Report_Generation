import requests
import json

def fetch_data():
    # Fake API endpoint and credentials
    api_endpoint = "https://api.bigmaker.com/events"
    api_key = "FAKE_API_KEY"

    # Fetch data from the API
    response = requests.get(api_endpoint, headers={"Authorization": f"Bearer {api_key}"})
    data = response.json()

    # Save data to a file for further processing
    with open('data/raw_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    fetch_data()
