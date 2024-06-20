import pandas as pd
import re

def clean_and_transform_data(data):
    df = pd.DataFrame(data)
    df['event_date'] = pd.to_datetime(df['event_date'])
    df['participants'] = df['participants'].apply(lambda x: re.sub(r'\D', '', str(x)))
    return df
