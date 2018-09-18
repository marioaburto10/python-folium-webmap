# importing folium dependency that will be used to
import folium

# using the Map method to create a web map at the specified location, in this case Wshington DC. Have the map render already zoomed in with a specific tile style
map = folium.Map(location=[38.926702, -77.018698], zoom_start=6, tiles="Mapbox Bright") 

# create a pop up marker at a certain location with a message and add it to the map
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[38.91, -77.2], popup="Hi I am a Marker", icon=folium.Icon(color="green")))
map.add_child(fg)

# this will generate a web map and save it as an html file
map.save("Map1.html");