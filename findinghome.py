import openrouteservice
import json
import csv
import time

towns = []

departement = '63'
where_you_work = (3.139185,45.788227)
api_key = 'API_KEY' # Specify your personal API key

class Town:
  def __init__(self, code_postal, name, lat, longi):
    self.code_postal = code_postal
    self.name = name
    self.lat = lat
    self.longi = longi
    self.travel_time = None

with open('laposte_hexasmal.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
      data = row[0].split(";")
      if data[0].startswith(departement):
        if len(data) == 6:
          lat, longi = data[5].split(",")
          towns.append(Town(data[0], data[1], lat, longi))

with open('towns.csv', 'w', newline='') as csvfile:
  client = openrouteservice.Client(key=api_key) 

  for town in towns:
    coords = (where_you_work, (town.longi, town.lat))
    try:
      routes = client.directions(coords)
      town.travel_time = routes["routes"][0]["summary"]["duration"]

      spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow([town.name, town.code_postal, town.travel_time])
      print("{} {} ({},{}) = {:.0f} minutes".format(town.name, town.code_postal, town.longi, town.lat, town.travel_time / 60))
    except Exception as e:
      print(e)
    time.sleep(2.0)
