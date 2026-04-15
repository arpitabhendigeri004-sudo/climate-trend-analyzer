from src.eda import plot_anomalies
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.eda import plot_temperature
from src.trend import add_trend
from src.anomaly import detect_anomaly
from src.forecasting import forecast


print("🚀 Starting Climate Trend Analyzer...")

df = load_data("data/raw/climate.csv")
print("✅ Data Loaded")

df = preprocess(df)
print("✅ Data Preprocessed")

plot_temperature(df)
print("📊 Graph Generated")

df = add_trend(df)

df = detect_anomaly(df)
plot_anomalies(df)
print("🚨 Anomaly Detection Done")

future = forecast(df)

print("\n📊 Forecasted Temperature Values:\n")
print(future)

print("\n📋 Final Data Preview:\n")
print(df.head())