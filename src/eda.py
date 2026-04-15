import matplotlib.pyplot as plt

def plot_temperature(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Temperature'], color='blue')
    plt.title("Temperature Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.grid()

    plt.savefig("outputs/graphs/temp_trend.png")
    plt.show()


def plot_anomalies(df):
    plt.figure(figsize=(10,5))

    # Normal line
    plt.plot(df['Date'], df['Temperature'], label='Temperature', color='blue')

    # Anomalies
    anomalies = df[df['Anomaly'] == 1]
    plt.scatter(anomalies['Date'], anomalies['Temperature'], 
                color='red', label='Anomalies', s=100)

    plt.title("Temperature with Anomalies")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.legend()
    plt.grid()

    plt.savefig("outputs/graphs/anomaly_plot.png")
    plt.show()