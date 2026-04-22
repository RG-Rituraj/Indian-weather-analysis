import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Create Karna (Assam, Delhi, Uttarakhand, Bangalore)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] * 4,
    'State': ['Delhi']*12 + ['Assam']*12 + ['Uttarakhand']*12 + ['Bangalore']*12,
    'Avg_Temp': [
        14, 18, 25, 32, 36, 34, 31, 30, 29, 26, 20, 15, # Delhi (Extreme)
        18, 20, 24, 26, 28, 29, 30, 30, 29, 27, 23, 19, # Assam (Humid)
        7, 10, 15, 19, 22, 24, 23, 23, 21, 17, 12, 8,   # Uttarakhand (Cold)
        21, 23, 26, 28, 27, 24, 23, 23, 23, 23, 22, 21  # Bangalore (Pleasant)
    ]
}

df = pd.DataFrame(data)

# 2. Visualizing the Data (Graph Banana)
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Month', y='Avg_Temp', hue='State', marker='o', linewidth=2.5)

# 3. Styling (Project ko sundar banane ke liye)
plt.title('Annual Temperature Trends: State-wise Comparison (2025-26)', fontsize=16)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Average Temperature (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Regions')

# Save the plot to show in your project
plt.savefig('weather_analysis_chart.png')
plt.show()

# 4. Simple Insights (Jo tum project file mein likh sakte ho)
print("Analysis Summary:")
for state in df['State'].unique():
    max_t = df[df['State'] == state]['Avg_Temp'].max()
    min_t = df[df['State'] == state]['Avg_Temp'].min()
    print(f"- {state}: Max Temp {max_t}°C, Min Temp {min_t}°C")