import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Display basic info
print("First 5 rows:\n", df.head())
print("\nDataset Info:\n")
print(df.info())

print("\nStatistical Summary:\n", df.describe())

# Unemployment trend over time
plt.figure(figsize=(12,5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df)
plt.title("Unemployment Rate Over Time (India)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# Covid-19 period (2020)
covid = df[df['Date'].dt.year == 2020]

plt.figure(figsize=(12,5))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=covid)
plt.title("Unemployment Rate During Covid-19 (2020)")
plt.show()

# State-wise average unemployment
state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values()

plt.figure(figsize=(14,6))
state_avg.plot(kind='bar')
plt.title("Average Unemployment Rate by State")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# Month-wise trend (seasonal pattern)
df['Month'] = df['Date'].dt.month
month_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))
month_avg.plot(kind='line', marker='o')
plt.title("Monthly Average Unemployment Trend")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.show()