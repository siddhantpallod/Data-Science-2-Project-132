import matplotlib.pyplot as plt
import csv

rows = []

with open('detail.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.reader(f)

    for row in reader :
        rows.append(row)

headers = rows[0]
planetData = rows[1:]

names = []
masses = []
radiuses = []
gravity = []

for data in planetData:
    if len(planetData) == 4:
        names.append(planetData[1])
        masses.append(planetData[3])
        radiuses.append(planetData[4])
        gravity.append(planetData[5])

masses.sort()
radiuses.sort()
gravity.sort()

plt.plot(radiuses, masses)
plt.title('Planet Radius and Mass')
plt.xlabel("Radius")
plt.ylabel('Mass')
plt.show()