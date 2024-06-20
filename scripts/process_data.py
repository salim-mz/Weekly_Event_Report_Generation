import pandas as pd
import json
import re

def process_data():
    # Load raw data
    with open('data/raw_data.json', 'r') as f:
        data = json.load(f)

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Clean and process data
    df['event_date'] = pd.to_datetime(df['event_date'])
    df['participants'] = df['participants'].apply(lambda x: re.sub(r'\D', '', str(x)))

    # Save processed data
    df.to_csv('data/processed_data.csv', index=False)

if __name__ == "__main__":
    process_data()
