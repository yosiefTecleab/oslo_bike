import requests
import json

url_availability = "https://oslobysykkel.no/api/v1/stations/availability"
headers = {'Client-Identifier': identifier}
response_availability = requests.get(url_availability, headers=headers)
availability = response_availability.json()

url_stations=" https://oslobysykkel.no/api/v1/stations"
headers = {'Client-Identifier': identifier}
response_stations = requests.get(url_stations, headers=headers)
stations = response_stations.json()

id_station ={}
for station in stations:
	id_station[station['id']]=station['title']


yyyymmdd = availability['updated_at'].split('T')[0]
time = availability['updated_at'].split('T')[1]

print("updated: yyymmdd "+yyyymmdd +"\n"+"updated: time "+time)
      
for available in availability:
	for st in range(len(stations)-1):
		if availability['stations'][st]['id'] in id_station:
			id=availability['stations'][st]['id']
			station=id_station[availability['stations'][st]['id']]
			Available_locks=availability['stations'][st]['availability']['locks']
			Available_bikes=availability['stations'][st]['availability']['bikes']
			
			print("id: "+str(id) + " station: "+station +" Available locks: "+str(Available_locks)
			+" Available bikes: "+str(Available_bikes))
			
print("updated: yyymmdd "+yyyymmdd +"\n"+"updated: time "+time)
