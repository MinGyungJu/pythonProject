import folium

map_osm = folium.Map(location=[37.572807,126.975918],
                     zoom_start=17)
folium.Marker(location=[39.032,125.7539155],
              popup='세종문화회관').add_to(map_osm)
                     #tiles='Stamen Toner') #16~19
map_osm.save('./map/map2.html')