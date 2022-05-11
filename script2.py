import csv

minutes = 30

with open('puy_de_dome.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
      data = row[0].split(",")
      if float(data[2]) < minutes * 60:
        print(data[0], data[1])