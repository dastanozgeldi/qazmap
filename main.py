import json
import folium
import streamlit as st
from streamlit_folium import st_folium

from popup import generate_popup

st.set_page_config(layout="wide")

with open("data.json") as f:
    data = json.load(f)

# map = folium.Map(location=data[0]['place'], zoom_start=5)
map = folium.Map(location=[48.0196, 66.9237], zoom_start=5)

for person in data:
    location = person['place'][0], person['place'][1]
    folium.Marker(location, popup=generate_popup(person)).add_to(map)

# highlight Kazakhstan
with open('kz.geojson', 'r') as f:
    geojson_data = f.read()

folium.GeoJson(geojson_data).add_to(map)

st_folium(map, width="100%")
