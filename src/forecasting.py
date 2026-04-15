from statsmodels.tsa.arima.model import ARIMA

def forecast(df):
    model = ARIMA(df['Temperature'], order=(1,1,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=6)
    return forecast