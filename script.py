import openrouteservice
import json
import csv
import time

towns = []

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
      if data[0].startswith('63'):
        if len(data) == 6:
          lat, longi = data[5].split(",")
          towns.append(Town(data[0], data[1], lat, longi))


print(len(towns))

with open('towns.csv', 'w', newline='') as csvfile:
  client = openrouteservice.Client(key='5b3ce3597851110001cf6248220c3396d2f14104876b229138ac3a45') # Specify your personal API key
  brezet = (3.139185,45.788227)

  for town in towns:
    print(town.name, town.longi, town.lat, town.code_postal)

    coords = (brezet,(town.longi, town.lat))
    try:
      routes = client.directions(coords)
      town.travel_time = routes["routes"][0]["summary"]["duration"]

      spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
      spamwriter.writerow([town.name, town.code_postal, town.travel_time])
    except:
      print("error")
    time.sleep(2.0)
