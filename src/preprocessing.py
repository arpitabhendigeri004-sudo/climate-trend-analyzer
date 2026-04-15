import pandas as pd

def preprocess(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df = df.ffill()
    return df