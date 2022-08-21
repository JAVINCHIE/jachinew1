import folium
import pandas
data = pandas.read_csv('Volcanoes_USA.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58,-99.09], zoom_start=6, tiles="OpenStreetMap" )# zoom_start for zooming on the mapp
fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln],popup=str(el)+'m', icon=folium.Icon(color=color_producer(el))))




map.add_child(fg)
map.save('map123.html')