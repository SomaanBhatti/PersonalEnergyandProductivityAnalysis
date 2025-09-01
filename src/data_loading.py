import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV files
print("\n\n")

# Load hourly data
hourly_df = pd.read_csv('data/raw/PAD_Hourly_Data.csv')
print(f"Hourly data shape: {hourly_df.shape}")
print("Hourly data columns:", list(hourly_df.columns))

# Load daily summary
daily_df = pd.read_csv('data/raw/PAD_Daily_Summary.csv')
print(f"\nDaily data shape: {daily_df.shape}")
print("Daily data columns:", list(daily_df.columns))

# Load weather data
weather_df = pd.read_csv('data/raw/PAD_weather_data_6-26AUG.csv')
print(f"\nWeather data shape: {weather_df.shape}")
print("Weather data columns:", list(weather_df.columns))


average_energy = hourly_df['Energy_level'].mean()
print(f"\nAverage Energy: {average_energy:.2f}")

most_common_mood = hourly_df['Mood'].mode()[0]
print(f"Most Common Mood: {most_common_mood}")

most_common_activity = hourly_df['Current_Activity'].mode()[0]
print(f"Most Common Activity: {most_common_activity}")

most_common_location = hourly_df['Location'].mode()[0]
print(f"Most Common Location: {most_common_location}")

sum_productive_tasks = hourly_df['Num_Productive_tasks'].sum()
print(f"Sum of Productive tasks: {sum_productive_tasks:.0f}")

sum_productive_hours = daily_df['Total_Productive_Hrs'].sum()
print(f"Sum of Productive hours: {sum_productive_hours:.0f}")