# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Create a figure
plt.figure(figsize=(10, 6))

# Initialize Basemap (projection type: 'mill' = Miller Cylindrical)
m = Basemap(projection='mill',
            llcrnrlat=-60, urcrnrlat=90,   # latitude range
            llcrnrlon=-180, urcrnrlon=180, # longitude range
            resolution='c')                # c = crude, l = low, i = intermediate, h = high

# Draw map features
m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawmapboundary(fill_color='lightblue')
m.fillcontinents(color='lightgreen', lake_color='lightblue')

# Add title
plt.title("World Map with Basemap (Miller Projection)")

# Show plot
plt.show()