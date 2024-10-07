import json
import folium
import streamlit as st
from streamlit_folium import st_folium

from popup import generate_popup

st.set_page_config(layout="wide")

with open("data.json") as f:
    data = json.load(f)

with open("writers.json") as f:
    writers = json.load(f)

col1, col2 = st.columns([1, 3])

with col1:
    with st.container(border=True):
        for era, people in writers.items():
            expander = st.expander(era)
            for person in people:
                expander.write(f'{person["name"]} ({person["lived"]})')

with col2:
    map = folium.Map(location=[48.0196, 66.9237], zoom_start=5)

    for person in data:
        location = person['place'][0], person['place'][1]
        folium.Marker(location, popup=generate_popup(person)).add_to(map)

    # highlight Kazakhstan
    with open('kz.json', 'r') as f:
        geojson_data = f.read()

    folium.GeoJson(geojson_data).add_to(map)

    st_folium(map, width="100%")
