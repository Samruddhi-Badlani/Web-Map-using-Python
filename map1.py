import folium
import pandas
map = folium.Map(location=[38.6,-99.2],zoom_start=6,tiles = "Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elevation = list(data["ELEV"])
location = list(data["LOCATION"])
def color_maker(el):
    if el >=0 and el <=1000:
        return 'green'
    elif el <=3000 :
        return 'orange'
    else:
        return 'red'
for lt, ln, el in zip(lat,lon,elevation):
    fgv.add_child(folium.Marker(location=[lt,ln],popup="%s m" % el,icon = folium.Icon(color=color_maker(el))))

fgp.add_child(folium.GeoJson(data = open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x : { 'fillColor':'yellow' if x['properties']['POP2005'] < 10000000 
else 'orange' if  10000000<=x['properties']['POP2005']<=20000000 else 'red'}))
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("map1.html")