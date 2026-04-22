import matplotlib.pyplot as plt
import pandas as pd

# Data for multiple states across India
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Delhi': [25.5, 26.1, 25.8, 26.5, 27.2],
    'Mumbai': [27.2, 27.5, 27.3, 27.8, 28.1],
    'Uttarakhand': [14.2, 14.8, 14.5, 15.1, 15.6],
    'Bangalore': [23.8, 24.1, 23.9, 24.5, 24.8],
    'Pune': [24.5, 25.0, 24.8, 25.3, 25.9],
    'Hyderabad': [26.8, 27.2, 27.0, 27.6, 28.0],
    'Sikkim': [12.5, 13.1, 12.8, 13.4, 13.9],
    'Madhya Pradesh': [25.0, 25.6, 25.3, 26.0, 26.7]
}

df = pd.DataFrame(data)

# Plotting settings
plt.figure(figsize=(12, 7))

for state in df.columns[1:]:
    plt.plot(df['Year'], df[state], marker='o', label=state, linewidth=2)

plt.title('Average Annual Temperature Trends (State-wise)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.xticks(df['Year'])
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='States', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

# Saving the updated graph
plt.savefig('india_weather_analysis.png')
print("Naya graph 'india_weather_analysis.png' ke naam se save ho gaya hai!")
plt.show()