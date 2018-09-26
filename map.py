# importing folium dependency that will be used to dynamically build my web map
import folium
# importing pandas to do some data processing
import pandas

# using pandas to read and bring in our text file with all our volcano data
data = pandas.read_csv("assets/data/volcano_data.txt")

# extract certain columns from the data file and turn them into lists so that we can interate through them
lat = list(data["LAT"])
lng = list(data["LON"])
elev = list(data["ELEV"])

# using the Map method to create a web map at the specified location, in this case Sacramento, CA. Have the map render already zoomed in with a specific tile style
map = folium.Map(location=[38.554587, -121.511129], zoom_start=6, tiles="Mapbox Bright") 

# function that will return a color depending on the numerical value of the elevation of each volcano
def maker_color_picker(elevation):
	if elevation < 1000:
		return 'green'
	elif 1000 <= elevation < 3000:
		return 'orange'
	else:
		return 'red'

# create a feature group using folium to add markers on the map
fg_v = folium.FeatureGroup(name="Volcanoes")

# use a for loop to iterate through every latitude, longitude, and elevation
# use the key word zip to be able to pass in three lists and be able to iterate through all three at the same time
for lt, lg, el in zip(lat, lng, elev):
	# create a circle pop up marker at a certain location with a message of each volcano elevation and add it to the map
	fg_v.add_child(folium.CircleMarker(location=[lt, lg], radius=8, popup=str(el)+" meters", fill=True, fill_color=maker_color_picker(el), color="grey", fill_opacity=0.7))

# create another feature group to add a layer for population on the map
fg_p = folium.FeatureGroup(name="Population")

# adding GeoJson Polygon layer to the map by reading the world.json file
# it will create a polygon layer and the polygon color will be based on population
fg_p.add_child(folium.GeoJson(data=open("assets/data/world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red" }))

# add both feature groups to the map
map.add_child(fg_p)
map.add_child(fg_v)

# add functionality to the map to allow us to manually turn each layer off and on
map.add_child(folium.LayerControl())

# generate a web map and save it as an html file
map.save("Map.html")
