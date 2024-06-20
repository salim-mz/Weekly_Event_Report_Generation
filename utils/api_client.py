import requests

def fetch_data_from_api(api_endpoint, api_key):
    response = requests.get(api_endpoint, headers={"Authorization": f"Bearer {api_key}"})
    return response.json()
