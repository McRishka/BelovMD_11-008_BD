import json

with open('Uber-Taxi.txt', 'r') as file:
    data = json.load(file)

f_name = input()
f_data = input()

for cl in data['Clients']:
    if cl['name'] == f_name:
        f_id = cl['client_id']
        break

trips = []
for tr in data["Trips"]:
    if tr['client_id'] and tr['date'] == f_data:
        trips.append(tr)
print(trips)
