import folium
from folium.plugins import MarkerCluster


def make_map(df, incident):
    """ Make an interactive map using folium. For a certain incident there will be clusters of its occurences. """

    tup = tuple(df[['Lat', 'Long']].iloc[0])
    m = folium.Map(location=tup)
    locations = []
    for index, row in df.iterrows():
        if row['OFFENSE_CODE_GROUP'] == incident:
            locations.append(tuple(row[['Lat', 'Long']]))

    incid = folium.FeatureGroup(name='Incidents')
    incid.add_child(MarkerCluster(locations=locations))
    m.add_child(incid)
    m.save('map.html')
