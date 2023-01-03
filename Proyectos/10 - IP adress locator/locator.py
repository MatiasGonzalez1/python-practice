import geocoder as geo

ip_address = geo.ip('me')
print(ip_address)
 #insert your ip
ip = geo.ip('190.xxx.xxx.x')
print(ip.city)

print(ip.latlng)

info = geo.google('San Francisco')
print(info.geojson)
print(info.osm)
print(info.wkt)