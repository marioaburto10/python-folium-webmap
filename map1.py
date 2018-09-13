# importing folium dependency that will be used to
import folium

# using the Map method to create a web map at the specified location, in this case Wshington DC
map = folium.Map(location=[38.926702, -77.018698]) 
# this will generate a web map and save it as an html file
map.save("Map1.html");