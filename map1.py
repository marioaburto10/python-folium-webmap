# importing folium dependency that will be used to
import folium
# importing pandas to do some data processing
import pandas

# using pandas to read and bring in our text file with all our volcano data
data = pandas.read_csv("Resources/volcano_data.txt")

# extract certain columns from the data file and turn them into lists so that we can interate through them
lat = list(data["LAT"])
lng = list(data["LON"])
elev = list(data["ELEV"])

# using the Map method to create a web map at the specified location, in this case Sacramento, CA. Have the map render already zoomed in with a specific tile style
map = folium.Map(location=[38.554587, -121.511129], zoom_start=6, tiles="Mapbox Bright") 

# create a feature froup using folium to create our markers on the map
fg = folium.FeatureGroup(name="My Map")

# use a for loop to iterate through every latitude, longitude, and elevation
# use the key word zip to be able to pass in three lists and be able to iterate through all three at the same time
for lt, lg, el in zip(lat, lng, elev):
	# create a pop up marker at a certain location with a message of each volcano elevation and add it to the map
	fg.add_child(folium.Marker(location=[lt, lg], popup=str(el)+" meters", icon=folium.Icon(color="green")))

# add each dynamically created feature group (marker) to the map
map.add_child(fg)

# generate a web map and save it as an html file
map.save("Map1.html")