import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.preprocessing import preprocess
from src.trend import add_trend
from src.anomaly import detect_anomaly

st.set_page_config(page_title="Climate Trend Analyzer", layout="wide")

st.title("🌍 Climate Trend Analyzer Dashboard")

# Load data
df = load_data("data/raw/climate.csv")
df = preprocess(df)
df = add_trend(df)
df = detect_anomaly(df)

# Show data
st.subheader("📊 Dataset Preview")
st.dataframe(df)

# Temperature Trend
st.subheader("📈 Temperature Trend")
fig1, ax1 = plt.subplots()
ax1.plot(df['Date'], df['Temperature'], color='blue')
ax1.set_title("Temperature Over Time")
st.pyplot(fig1)

# Anomaly Detection
st.subheader("🚨 Anomaly Detection")

fig2, ax2 = plt.subplots()
ax2.plot(df['Date'], df['Temperature'], label='Temperature')

anomalies = df[df['Anomaly'] == 1]
ax2.scatter(anomalies['Date'], anomalies['Temperature'], color='red', label='Anomalies')

ax2.legend()
ax2.set_title("Anomaly Detection")

st.pyplot(fig2)

st.success("✅ Dashboard Running Successfully!")