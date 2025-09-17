import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Load your CSV files

# Load hourly data
hourly_df = pd.read_csv('data/raw/PAD - Hourly_Data.csv')
# print(f"Hourly data shape: {hourly_df.shape}")
# Should return (495, 10). 495 rows and 10 columns
# print("Hourly data columns:", list(hourly_df.columns))
# Returns the list of column names

# Load daily summary
daily_df = pd.read_csv('data/raw/PAD - Daily_Summary.csv')
# print(f"\nDaily data shape: {daily_df.shape}")
# returns (33, 6)
# print("Daily data columns:", list(daily_df.columns))

# Load weather data
weather_df = pd.read_csv('data/raw/PAD - Weather_Data.csv')
# print(f"\nWeather data shape: {weather_df.shape}")
# returns (816,7)
# print("Weather data columns:", list(weather_df.columns))

print("\n=== BASIC STATISTICS ===\n")
average_energy = hourly_df['Energy_level'].mean()
print(f"Average Energy: {average_energy:.2f}")

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

average_sleep_q = daily_df['Sleep_Quality (1-10)'].mean()
print(f"Average Sleep Quality: {average_sleep_q:.2f}")

hourly_df['DateTime'] = pd.to_datetime(hourly_df['DateTime'], format='%d-%m-%Y %H:%M')
hourly_df['Date'] = hourly_df['DateTime'].dt.date
hourly_df['DayOfWeek'] = hourly_df['DateTime'].dt.day_name()

print("\n=== ENERGY PATTERNS ===\n")
# What time of day do you have highest/lowest energy?
hourly_df['Hour'] = hourly_df['DateTime'].dt.hour
energy_by_hour = hourly_df.groupby('Hour')['Energy_level'].mean()
print(f"Highest energy at: {energy_by_hour.idxmax()}:00 (avg: {energy_by_hour.max():.1f})")
print(f"Lowest energy at: {energy_by_hour.idxmin()}:00 (avg: {energy_by_hour.min():.1f})")

hourly_df['DayOfWeek'] = hourly_df['DateTime'].dt.day_name()

print("\n=== WEEKLY PATTERN ANALYSIS ===\n")

# Create day-of-week summaries
weekly_summary = hourly_df.groupby('DayOfWeek').agg({
    'Energy_level': 'mean',
    'Procrastination_Score': 'mean',
    'Num_Productive_tasks': 'mean',
}).round(2)

# Add most common activity and location for each day of week
for day in weekly_summary.index:
    day_data = hourly_df[hourly_df['DayOfWeek'] == day]
    most_common_activity = day_data['Current_Activity'].mode()[0] if not day_data['Current_Activity'].empty else 'None'
    most_common_location = day_data['Location'].mode()[0] if not day_data['Location'].empty else 'None'
    weekly_summary.loc[day, 'Top_Activity'] = most_common_activity
    weekly_summary.loc[day, 'Top_Location'] = most_common_location

# Reorder to start with Monday
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly_summary = weekly_summary.reindex([day for day in day_order if day in weekly_summary.index])

# Create PrettyTable
table = PrettyTable()
table.field_names = ["Day", "Avg Energy", "Avg Procrastination", "Avg Tasks/Hour", "Top Activity", "Top Location"]

# Add rows to table
for day in weekly_summary.index:
    table.add_row([
        day,
        f"{weekly_summary.loc[day, 'Energy_level']:.1f}",
        f"{weekly_summary.loc[day, 'Procrastination_Score']:.1f}",
        f"{weekly_summary.loc[day, 'Num_Productive_tasks']:.2f}",
        weekly_summary.loc[day, 'Top_Activity'],
        weekly_summary.loc[day, 'Top_Location']
    ])

print(table)