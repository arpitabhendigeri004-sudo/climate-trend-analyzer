import numpy as np

def detect_anomaly(df):
    mean = np.mean(df['Temperature'])
    std = np.std(df['Temperature'])

    df['Z_score'] = (df['Temperature'] - mean)/std
    df['Anomaly'] = df['Z_score'].apply(lambda x: 1 if abs(x) > 1.5 else 0)

    return df