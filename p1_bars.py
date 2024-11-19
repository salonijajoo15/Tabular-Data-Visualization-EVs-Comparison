import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('evs_assignment1.xlsx')
print(df)
min_bin = 100
max_bin = 280
interval_width = 40
efficiency_intervals = np.arange(min_bin, max_bin + interval_width, interval_width)
df['Efficiency Interval'] = pd.cut(df['Efficiency'], bins=efficiency_intervals)
car_counts = df.groupby(['Efficiency Interval', 'Region']).size().reset_index(name='Count')
car_counts['Efficiency Interval'] = car_counts['Efficiency Interval'].astype(str)
regions = ['America', 'Asia', 'Europe']
colors = {'America': 'yellow', 'Asia': 'pink', 'Europe': 'navy'}
total = df['Region'].value_counts()
car_counts['Relative Count'] = car_counts.apply(lambda row: row['Count'] / total[row['Region']], axis=1)
intervals_labels = car_counts['Efficiency Interval'].unique()
x = np.arange(len(intervals_labels)) 
width = 0.2  

# Plot the data
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
for i, region in enumerate(regions):
    region_data = car_counts[car_counts['Region'] == region]
    axes[0].bar(x + i * width, region_data['Count'], width, color=colors[region], label=region)

axes[0].set_title('Efficiency of EVs produced between 2010 and 2024')
axes[0].set_xlabel('Efficiency in Wh/km')
axes[0].set_ylabel('Nuber of EV models')
axes[0].set_xticks(x + width)
axes[0].set_xticklabels(intervals_labels, rotation=45)
axes[0].legend(title='Production Region')

#graph 2
for i, region in enumerate(regions):
    region_data = car_counts[car_counts['Region'] == region]
    axes[1].bar(x + i * width, region_data['Relative Count'], width, color=colors[region], label=region)

axes[1].set_title('Efficiency of EVs produced between 2010 and 2024')
axes[1].set_xlabel('Efficiency in Wh/km')
axes[1].set_ylabel('Proportion of EV models')
axes[1].set_xticks(x + width)
axes[1].set_xticklabels(intervals_labels, rotation=45)
axes[1].legend(title='Production Region')

plt.tight_layout()
plt.show()