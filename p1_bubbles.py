import pandas as pd
import matplotlib.pyplot as plt
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Create a dynamic bubble chart to visualize EV characteristics.')
parser.add_argument('-i', '--input', required=True, help='Input Excel file containing the dataset')
parser.add_argument('-x', required=True, help='Attribute for x-axis')
parser.add_argument('-y', required=True, help='Attribute for y-axis')
parser.add_argument('-c', required=True, help='Attribute for color encoding')
parser.add_argument('-s', required=True, help='Attribute for bubble size')
args = parser.parse_args()  

df = pd.read_excel('evs_assignment1.xlsx')
print(df)
x = df[args.x]
y = df[args.y]
color_attr = df[args.c]
size_attr = df[args.s]
size = (size_attr - size_attr.min()) / (size_attr.max() - size_attr.min()) * 1000  

#plotting bubble chart
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, s=size, c=color_attr, cmap='viridis', alpha=0.6, edgecolors='w', linewidth=0.5)
cbar = plt.colorbar(scatter)
cbar.set_label(args.c)
plt.title(f'Bubble Chart of EVs: {args.x} vs {args.y}')
plt.xlabel(args.x)
plt.ylabel(args.y)
for size_val in [100, 500, 1000]:
    plt.scatter([], [], s=size_val, c='gray', alpha=0.5, edgecolor='w', linewidth=0.5, label=f'Size: {size_val}')
plt.legend(scatterpoints=1, frameon=True, labelspacing=1, title=args.s)

plt.tight_layout()
plt.show()
