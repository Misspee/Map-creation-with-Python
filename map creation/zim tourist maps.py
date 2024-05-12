# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:41:13 2024

@author: dell
"""

import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


 #load shapefile
tourist_sites = gpd.read_file("C:/Users/dell/Desktop/Women in GIS mentorship/touristsites.shp")
 #create a base map of Zimbabwe
world=gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
zimbabwe= world[world.name=='Zimbabwe']
 
 #plot basemap
ax=zimbabwe.plot(color='lightgray', edgecolor='white', figsize=(10,8))
ax.set_aspect('equal')
ax.set_axis_off()

 #plot tourist sites
tourist_sites.plot(ax=ax, marker='o', color='red',  markersize=100, label='Tourist Sites')
#add labels for each point
for x,y, label in zip(tourist_sites.geometry.x, tourist_sites.geometry.y, tourist_sites['Site_Names']):
    ax.text(x,y, label, fontsize= 8, ha='right')
#add legend
ax.legend()
#Add north arrow
arrow= FancyArrowPatch((0.85,0.92),(0.85,0.9), mutation_scale=15, color='black', label='North')
ax.add_patch(arrow)

#Set title
plt.title('Tourist Sites in Zimbabwe', fontsize=16)

#show the map
plt.show()
plt.savefig('touristsites.png', dpi= 200)


