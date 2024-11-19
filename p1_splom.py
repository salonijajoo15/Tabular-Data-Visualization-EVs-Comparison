import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

# Set up command line argument
parser = argparse.ArgumentParser(description='Create a scatter plot matrix (SPLOM) for visualizing correlations among multiple EV attributes.')
parser.add_argument('-i', '--input', required=True, help='Input Excel file containing the dataset')
parser.add_argument('-a', '--attributes', nargs='+', required=True, help='List of attributes to include in the scatter plot matrix (SPLOM)')
args = parser.parse_args()
df = pd.read_excel('evs_assignment1.xlsx')

#plottign scatter plot
region_colors = {'America': 'yellow', 'Asia': 'pink', 'Europe': 'navy'}
sns.set(style='whitegrid')
pair_plot = sns.pairplot(df, vars=args.attributes, hue='Region', palette=region_colors, diag_kind='kde', plot_kws={'alpha': 0.6, 's': 40, 'edgecolor': 'w'})
pair_plot.fig.suptitle('Scatter Plot Matrix of EV Attributes', y=1.02)
plt.show()
