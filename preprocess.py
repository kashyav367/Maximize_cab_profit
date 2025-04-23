# preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path)

    # Fill missing values
    df = df.dropna(subset=['price', 'surge_multiplier', 'distance', 'source', 'destination', 'cab_type'])

    # Extract features from timestamp
    df['time_stamp'] = pd.to_datetime(df['time_stamp'])
    df['hour'] = df['time_stamp'].dt.hour
    df['weekday'] = df['time_stamp'].dt.weekday

    # Encode categorical variables
    encoders = {}
    for col in ['cab_type', 'source', 'destination']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le

    features = df[['distance', 'surge_multiplier', 'cab_type', 'source', 'destination', 'hour', 'weekday']]
    target = df['price']

    return features, target, encoders, df
