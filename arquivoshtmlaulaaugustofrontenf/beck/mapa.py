import folium
import webbrowser

latitude = -26.67
longitude = -49.67
location = [latitude, longitude]
m = folium.Map(location=location, zoom_start=12, title='OpenStreetMap')

folium.Marker(
    location=[latitude, longitude],
    popup='<b></b>',
    tooltip='Click here'
).add_to(m)


m.save("map.html")