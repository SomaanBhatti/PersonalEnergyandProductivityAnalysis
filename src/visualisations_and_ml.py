import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
from prettytable import PrettyTable
from scipy.stats import pearsonr, spearmanr

# Set style for better looking plots
plt.style.use('default')  # Changed from seaborn-v0_8 to avoid compatibility issues
sns.set_palette("husl")

# Load and prepare data
hourly_df = pd.read_csv('data/raw/PAD - Hourly_Data.csv')
daily_df = pd.read_csv('data/raw/PAD - Daily_Summary.csv')

# Clean data first
print("=== DATA CLEANING ===")
print(f"Original data shape: {hourly_df.shape}")

# Remove any rows with missing critical values
hourly_df = hourly_df.dropna(subset=['Energy_level', 'Procrastination_Score'])
print(f"After removing missing values: {hourly_df.shape}")

# Check for any weird values
print(f"Energy level range: {hourly_df['Energy_level'].min()} to {hourly_df['Energy_level'].max()}")
print(f"Procrastination score range: {hourly_df['Procrastination_Score'].min()} to {hourly_df['Procrastination_Score'].max()}")

hourly_df['DateTime'] = pd.to_datetime(hourly_df['DateTime'], format='%d-%m-%Y %H:%M')
hourly_df['Hour'] = hourly_df['DateTime'].dt.hour
hourly_df['DayOfWeek'] = hourly_df['DateTime'].dt.day_name()
hourly_df['IsWeekend'] = hourly_df['DateTime'].dt.weekday >= 5

# Create figure with subplots
fig = plt.figure(figsize=(15, 12))

# 1. Energy levels throughout the day
plt.subplot(2, 3, 1)
energy_by_hour = hourly_df.groupby('Hour')['Energy_level'].mean()
plt.plot(energy_by_hour.index, energy_by_hour.values, marker='o', linewidth=2, markersize=6)
plt.title('Average Energy Levels Throughout the Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Energy Level')
plt.grid(True, alpha=0.3)

# 2. Correlation heatmap
plt.subplot(2, 3, 2)
numeric_cols = ['Energy_level', 'Procrastination_Score', 'Num_Productive_tasks', 'Hour']
correlation_matrix = hourly_df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, square=True)
plt.title('Correlation Matrix')

# 3. Activity distribution (top 6 activities only, excluding Sleep)
plt.subplot(2, 3, 3)
activity_counts = hourly_df['Current_Activity'].value_counts()
activity_counts = activity_counts.drop('Sleep', errors='ignore')  # remove Sleep safely
activity_counts = activity_counts.head(6)  # take top 6 after dropping

plt.pie(activity_counts.values, labels=activity_counts.index, autopct='%1.1f%%')
plt.title('Top Activities Distribution')

# 4. Energy vs Procrastination scatter (with safe trend line)
plt.subplot(2, 3, 4)
plt.scatter(hourly_df['Energy_level'], hourly_df['Procrastination_Score'], alpha=0.6, s=30)
plt.xlabel('Energy Level')
plt.ylabel('Procrastination Score')
plt.title('Energy vs Procrastination')

# Safe trend line calculation
try:
    # Only use complete cases for trend line
    complete_data = hourly_df[['Energy_level', 'Procrastination_Score']].dropna()
    if len(complete_data) > 10:  # Need enough data points
        z = np.polyfit(complete_data['Energy_level'], complete_data['Procrastination_Score'], 1)
        p = np.poly1d(z)
        x_trend = np.linspace(complete_data['Energy_level'].min(), complete_data['Energy_level'].max(), 100)
        plt.plot(x_trend, p(x_trend), "r--", alpha=0.8)
except:
    print("Trend line calculation skipped due to data issues")

# 5. Weekend vs Weekday energy comparison
plt.subplot(2, 3, 5)
weekend_energy = hourly_df[hourly_df['IsWeekend']]['Energy_level'].dropna()
weekday_energy = hourly_df[~hourly_df['IsWeekend']]['Energy_level'].dropna()
if len(weekend_energy) > 0 and len(weekday_energy) > 0:
    plt.boxplot([weekday_energy, weekend_energy], labels=['Weekdays', 'Weekends'])
    plt.title('Energy: Weekdays vs Weekends')
    plt.ylabel('Energy Level')

# 6. Daily productivity trend
plt.subplot(2, 3, 6)

# Group daily productivity
daily_productivity = hourly_df.groupby(hourly_df['DateTime'].dt.date)['Num_Productive_tasks'].sum()
dates = pd.to_datetime(daily_productivity.index)
values = daily_productivity.values

# Map weekdays to colors
weekday_colors = {
    0: "green",    # Monday
    1: "blue",     # Tuesday
    2: "orange",   # Wednesday
    3: "red",      # Thursday
    4: "purple",   # Friday
    5: "brown",    # Saturday
    6: "pink"      # Sunday
}

# Plot per weekday (dots + connecting line)
for wd, color in weekday_colors.items():
    mask = dates.weekday == wd
    plt.plot(dates[mask], values[mask], marker='o', color=color, alpha=0.7, label=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][wd])

plt.title('Daily Productivity Trend')
plt.xlabel('Date')
plt.ylabel('Total Daily Tasks')
plt.xticks(rotation=45)

# Legend (no duplicates)
plt.legend(title="Day of Week", bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('data/processed/visualisations/personal_analytics_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n=== MACHINE LEARNING: ENERGY LEVEL PREDICTION ===")

# Prepare clean data for ML
ml_df = hourly_df.dropna(subset=['Energy_level', 'Procrastination_Score', 'Current_Activity', 'Location']).copy()

if len(ml_df) > 50:  # Need enough data for ML
    # Encode categorical variables
    le_activity = LabelEncoder()
    le_location = LabelEncoder()
    
    ml_df['Activity_encoded'] = le_activity.fit_transform(ml_df['Current_Activity'])
    ml_df['Location_encoded'] = le_location.fit_transform(ml_df['Location'])
    
    # Features for predicting energy level
    features = ['Hour', 'Procrastination_Score', 'Activity_encoded', 'Location_encoded']
    X = ml_df[features]
    y = ml_df['Energy_level']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train Random Forest model
    rf_model = RandomForestRegressor(n_estimators=50, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = rf_model.predict(X_test)
    
    # Evaluate model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Performance:")
    print(f"Mean Squared Error: {mse:.3f}")
    print(f"R² Score: {r2:.3f}")
    print(f"Model can explain {r2*100:.1f}% of energy level variance")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    for _, row in feature_importance.iterrows():
        print(f"{row['feature']}: {row['importance']:.3f}")

print("\n=== PROCRASTINATION HYPOTHESIS TEST ===")
# Test your original hypothesis
high_procrastination = hourly_df[hourly_df['Procrastination_Score'] >= 7]
low_procrastination = hourly_df[hourly_df['Procrastination_Score'] <= 3]

if len(high_procrastination) > 0 and len(low_procrastination) > 0:
    hypothesis_table = PrettyTable()
    hypothesis_table.field_names = ["Condition", "Avg Energy", "Sample Size"]
    hypothesis_table.add_row([
        "Low Procrastination (≤3)", 
        f"{low_procrastination['Energy_level'].mean():.2f}",
        len(low_procrastination)
    ])
    hypothesis_table.add_row([
        "High Procrastination (≥7)", 
        f"{high_procrastination['Energy_level'].mean():.2f}",
        len(high_procrastination)
    ])
    
    print(hypothesis_table)
    
    energy_difference = low_procrastination['Energy_level'].mean() - high_procrastination['Energy_level'].mean()
    print(f"\nEnergy difference: {energy_difference:+.2f}")
    print("✅ Lower procrastination = higher energy!" if energy_difference > 1 else "❌ Hypothesis not supported")
else:
    print("Not enough data in high/low procrastination categories for comparison")

print("\n=== PROCRASTINATION ↔ ENERGY CORRELATION ===")


# Drop rows with missing values just in case
df_corr = hourly_df[['Procrastination_Score', 'Energy_level']].dropna()

pearson_corr, pearson_p = pearsonr(df_corr['Procrastination_Score'], df_corr['Energy_level'])
spearman_corr, spearman_p = spearmanr(df_corr['Procrastination_Score'], df_corr['Energy_level'])

print(f"Pearson correlation: r = {pearson_corr:.2f}, p = {pearson_p:.4f}")
print(f"Spearman correlation: r = {spearman_corr:.2f}, p = {spearman_p:.4f}")

if pearson_p < 0.05 or spearman_p < 0.05:
    print("✅ Significant correlation found!")
else:
    print("❌ No significant correlation detected")