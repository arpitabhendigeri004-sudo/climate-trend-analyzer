def add_trend(df):
    df['Rolling_Mean'] = df['Temperature'].rolling(window=3).mean()
    return df