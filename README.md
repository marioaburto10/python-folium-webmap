# Building Web Maps With Folium!

#### In this project, I am using python as the base programming language and `map.py` as the center point of my app. I am using `pandas` to read and load my `volcano_data.txt` data file and I am using the package [folium](https://python-visualization.github.io/folium/docs-v0.6.0/) to dynamically create web maps. Folium allows us to manage our data in python and then helps us visualize it by using the [Leaflet.js](https://leafletjs.com/) library. This makes it super easy to build web maps in python without ever having to write any HTML, CSS, or Javascript code!

Upon opening `Map.html`, the map is centered around Sacramento, CA (location at 38.5816° N, 121.4944° W). By iterating through my `volcano_data.txt` file which has relevant information about volanoes in the USA, I am able to plot markers at the exact location of every volcano with pop-up information about the elevation of each volcano. The color of the marker is based on the elevation of the volcano. The color green indicates a volcano with an elevation less than 1000 meters, orange indicating an elevation between 1000 and 3000 meters, and red indicating any volcano with an elevation higher than 3000 meters.

<img src="https://github.com/marioaburto10/python-folium-webmap/blob/master/assets/images/volcanoMarkers.png?" width="400px" height="300px" />

On top of the marker layer, I added a polygon layer that color coated each country. The world country data is coming from `world.json` and the color of each country is based on the size of population. The color green signifies a country with a population less than 10 million people, orange signifies a country with population between 10 and 20 million, and any country with a population higher than 20 million is identified with the color red. I was able to accomplish this using a python `lambda` function along with `if/else` statements. 
```python
fg_p.add_child(folium.GeoJson(data=open("assets/data/world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red" }))
```
<img src="https://github.com/marioaburto10/python-folium-webmap/blob/master/assets/images/populationLayer.png" width="400px" height="200px" />

Lastly, I added layer control functionality to my map that allows me to turn the marker and population layer on and off. This is located on the top right of my map.
