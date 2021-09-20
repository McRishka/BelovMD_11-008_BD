class App:
    clients_number = 0
    drivers_number = 0
    trips_numbers = 0
    autoparks_numbers = 0

    clients_id = []
    drivers_id = []
    trips_id = []
    cars_numbers = []
    autoparks_id = []
    rates_set = set()

    def __init__(self, name):
        self.name = name


class Client:
    def __init__(self, my_app: App, name, rating, premium):
        my_app.clients_id.append(my_app.clients_number)
        self.client_id = my_app.clients_id[my_app.clients_number]
        my_app.clients_number += 1
        self.name = name
        self.rating = round(rating, 2)
        self.premium = premium


class Taxipark:
    cars_numbers = []
    drivers_list = []

    def __init__(self, my_app: App, name):
        self.name = name
        self.autopark_id = my_app.autoparks_numbers
        my_app.autoparks_id.append(self.autopark_id)
        my_app.autoparks_numbers += 1


class Driver:
    def __init__(self, my_app: App, name, rating, experience, car_number, autopark: Taxipark):
        my_app.drivers_id.append(my_app.drivers_number)
        self.driver_id = my_app.drivers_id[my_app.drivers_number]
        my_app.drivers_number += 1
        self.name = name
        self.rating = round(rating, 2)
        self.experience = experience
        self.car_number = car_number
        self.autopark_id = autopark.autopark_id
        autopark.cars_numbers.append(self.car_number)
        autopark.drivers_list.append(self.name)
        my_app.cars_numbers.append(self.car_number)


class Rates:
    def __init__(self, my_app: App, name, min_price):
        my_app.rates_set.add(name)
        self.name = name
        self.min_price = min_price


class Trip:
    def __init__(self, my_app: App, my_client: Client, my_driver: Driver, my_rates: Rates, date, time, distance):
        my_app.trips_id.append(my_app.trips_numbers)
        self.trip_id = my_app.trips_numbers
        my_app.trips_numbers += 1
        self.driver_id = my_driver.driver_id
        self.client_id = my_client.client_id
        self.my_rates = my_rates.name
        self.date = date
        self.time = time
        self.distance = distance

        if distance <= 1:
            self.coef = 1
        elif distance <= 3:
            self.coef = 1.5
        elif distance <= 6:
            self.coef = 1.8
        elif distance <= 10:
            self.coef = 2
        elif distance > 10:
            self.coef = 5

        if my_client.premium != True:
            self.price = round(self.coef * my_rates.min_price / (my_client.rating * 0.2), 2)
        else:
            self.price = round(self.coef * my_rates.min_price / (my_client.rating * 0.4), 2)
