import random
import json
import Class as taxi

Uber = taxi.App('Uber')
from datetime import date, time

eco = taxi.Rates(Uber, 'econom', 80)
business = taxi.Rates(Uber, 'business', 150, )
delivery = taxi.Rates(Uber, 'delivery', 120)
rates = [eco, delivery, business]
trips = []

drivers = []
clients = []
names = ['Grisha', 'Amir', 'Ramazan', 'Emma', 'Yana', 'Makar', 'Anya', 'Sergey', 'Timur', 'Sophia', 'Pasha',
         'Rasim', 'Almaz', 'Lilya', 'Kamilla', 'Sasha', 'Stalin', 'Lenin', 'Hitler', 'Putin']

saturn = taxi.Taxipark(Uber, 'Saturn')
cars_numbers = ['0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9']
rate = 5.0
exp = 8

for i in range(5):
    driver = taxi.Driver(Uber, random.choice(names), rate, f'{exp} years', cars_numbers.pop(0), saturn)
    drivers.append(driver)
    exp -= 1
    rate -= 0.1

premium = True
for name in range(5):
    client = taxi.Client(Uber, random.choice(names), rate, premium)
    clients.append(client)
    premium = -premium
    rate -= 0.1

for name in range(10):
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 28)
    random_hour = random.randint(0, 23)
    random_min = random.randint(0, 59)
    dist = random.randint(0, 13)
    trip = taxi.Trip(Uber, random.choice(clients), random.choice(drivers),
                     random.choice(rates), str(date(2021, random_month, random_day)),
                     str(time(random_hour, random_min)), dist)
    trips.append(trip)

example_client = taxi.Client(Uber, 'Makar', 5, True)
clients.append(example_client)
for i in range(5):
    dist = random.randint(0, 13)
    ex_trip = taxi.Trip(Uber, example_client, random.choice(drivers), random.choice(rates),
                        '2021-04-24',
                        str(time(random_hour, random_min)), dist)
    trips.append(ex_trip)
d_data = {}

d_data['App'] = []
d_data['Drivers'] = []
d_data['Clients'] = []
d_data['Rates'] = []
d_data['Trips'] = []
d_data['Taxipark'] = [{'name': saturn.name, 'autopark_id': saturn.autopark_id, 'cars_numbers': saturn.cars_numbers,
                       'drivers_list': saturn.drivers_list}]

d_data['App'].append({'name': Uber.name, 'clients_number': Uber.clients_number, 'clients_id': Uber.clients_id,
                      'trips_numbers': Uber.trips_numbers, 'trips_id': Uber.trips_id,
                      'drivers_number': Uber.drivers_number,
                      'autoparks_numbers': Uber.autoparks_numbers, 'drivers_id': Uber.drivers_id,
                      'cars_numbers': Uber.cars_numbers,
                      'autoparks_id': Uber.autoparks_id})

for i in range(len(rates)):
    d_data['Rates'].append({'name': rates[i].name, 'min_price': rates[i].min_price
                            })

for e in drivers:
    d_data['Drivers'].append({'name': e.name, "driver_id": e.driver_id, "autopark_id": e.autopark_id,
                              "rating": e.rating, "car_number": e.car_number, "experience": e.experience})

for e in clients:
    d_data['Clients'].append({'name': e.name, "client_id": e.client_id, "rating": e.rating, "premium": e.premium})

for e in trips:
    d_data['Trips'].append({'client_id': e.client_id, "driver_id": e.driver_id, "rate": e.my_rates,
                            'date': e.date, 'time': e.time, 'trip_id': e.trip_id, 'coef': e.coef,
                            'distance': e.distance})

with open('Uber-Taxi.txt', 'w') as file:
    json.dump(d_data, file)

print(1)
