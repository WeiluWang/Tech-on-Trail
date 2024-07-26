import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

# Load JSON data
file_path = 'accumulated_hiker_connections_2018.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract unique hikers
hikers = set()
for key in data.keys():
    hiker1, hiker2 = key.split(' <-> ')
    hikers.add(hiker1.strip())
    hikers.add(hiker2.strip())
hikers = sorted(hikers)

# Create a DataFrame for the interaction matrix
matrix = pd.DataFrame(0, index=hikers, columns=hikers)
for key, count in data.items():
    hiker1, hiker2 = key.split(' <-> ')
    matrix.at[hiker1.strip(), hiker2.strip()] = count
    matrix.at[hiker2.strip(), hiker1.strip()] = count

# Define the color palette
colors = ['black'] + sns.color_palette("YlOrRd", 20).as_hex() + ['darkred']
cmap = ListedColormap(colors)

# Define the color boundaries
boundaries = list(range(0, 420, 20)) + [matrix.values.max()]
norm = BoundaryNorm(boundaries, cmap.N, clip=True)

# Plot the heatmap
plt.figure(figsize=(12, 10))
ax = sns.heatmap(matrix, cmap=cmap, norm=norm, linewidths=.5, linecolor='gray', cbar_kws={'ticks': np.arange(0, 420, 20)})

# Customize the color bar
cbar = ax.collections[0].colorbar
cbar.set_ticks(np.arange(0, 420, 20))
cbar.set_ticklabels([str(i) for i in range(0, 400, 20)] + ['>400'])

plt.title('Hiker Interaction Matrix')
plt.xlabel('Hikers')
plt.ylabel('Hikers')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()
