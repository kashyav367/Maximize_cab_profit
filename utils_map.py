# utils_map.py

import folium
from streamlit_folium import st_folium

locations_dict = {
    'Haymarket Square': [42.3635, -71.0586],
    'Back Bay': [42.3503, -71.0810],
    'North End': [42.3656, -71.0542],
    'Beacon Hill': [42.3588, -71.0707],
    'Financial District': [42.3554, -71.0552],
    'Fenway': [42.3459, -71.0983]
}

def draw_route(source, destination, encoders):
    source_name = encoders['source'].inverse_transform([source])[0]
    dest_name = encoders['destination'].inverse_transform([destination])[0]
    source_loc = locations_dict.get(source_name, [42.3601, -71.0589])
    dest_loc = locations_dict.get(dest_name, [42.3611, -71.0579])

    m = folium.Map(location=source_loc, zoom_start=13)
    folium.Marker(source_loc, tooltip="Pickup", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(dest_loc, tooltip="Drop", icon=folium.Icon(color="red")).add_to(m)
    folium.PolyLine([source_loc, dest_loc], color="blue", weight=2.5, opacity=1).add_to(m)
    return m
