"""
Main module to analyze data provided by Twitter and build a map
"""

import folium
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="html_map")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def parse_json(data: dict) -> list:
    """
    Return list of lists with nicknames and location
    """
    list_of_friends = []
    for elements in data["users"]:
        if elements['location'] != '':
            list_of_friends.append(
                [elements['screen_name'], elements['location']])
    return list_of_friends


def get_coordinates(list_of_friends: list) -> list:
    """
    Return list of lists with nicknames and coordinates
    >>> get_coordinates([['_arsen', 'Kyiv']])
    [['_arsen', (50.4500336, 30.5241361)]]
    """
    coordinates = []
    for i, film in enumerate(list_of_friends):
        try:
            location = geolocator.geocode(film[1])
        except GeocoderUnavailable:
            continue
        if location is None:
            continue
        coordinates.append(
            [list_of_friends[i][0], (location.latitude, location.longitude)])
    return coordinates


def build_map(coordinates: list):
    """
    Build html file with map
    """
    main_map = folium.Map(
        location=[40.449718675169805, -5.577504695444702], zoom_start=3)
    folium.TileLayer('cartodbpositron').add_to(main_map)
    layer_map = folium.FeatureGroup(name="Map")
    for i in coordinates:
        layer_map.add_child(folium.Marker(
            location=[i[1][0], i[1][1]], popup=i[0], icon=folium.Icon(color='lightblue')))
    main_map.add_child(layer_map)
    return main_map._repr_html_()
