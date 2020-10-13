import datetime

get_datetime = lambda date_time_str: datetime.datetime.strptime(date_time_str, '%d.%m.%Y %H:%M:%S')

class Car():
    def __init__(self, name, seats, color):
        self.name = name
        self.seats = seats
        self.color = color
    def __str__(self):
        return "{} {} {}".format(self.name, self.seats, self.color)

class Cars(list):
    def add(self, car):
        self.append(car)
    def find(self, name):
        return next(x for x in self if x.name == name)

class Customer():
    def __init__(self, name, address, age):
        self.name = name
        self.seats = address
        self.color = age

class Booking:
    def __init__(self, car, begin, end):
        self.car = car
        self.begin = begin
        self.end = end

class CarBookings(list):
    def __init__(self, cars):
        self.cars = cars
    def book(self, car_name, begin, end):
        car = self.cars.find(car_name)
        booking = Booking(car, begin, end)
        self.cars.remove(car)
        self.append(booking)
        print()
        print('Booked for {}, car is no longer available from {} to {}'.format(car_name, begin, end))
        print('Available cars:')
        for i in self.cars:
            print(i)

car_data = [
    {
        'seats': 2,
        'color': 'black'
    },
    {
        'seats': 4,
        'color': 'grey'
    },
    {
        'seats': 7,
        'color': 'silver'
    }
]

cars = Cars()
for i in car_data:
    car = Car('{}-seater'.format(i['seats']), i['seats'], i['color'])
    cars.add(car)
for i in cars:
    print(i)


carBooking = CarBookings(cars)
carBooking.book('2-seater', get_datetime('01.11.2020 12:00:00'), get_datetime('05.11.2020 12:00:00'))
carBooking.book('7-seater', get_datetime('05.11.2020 12:00:00'), get_datetime('02.11.2020 12:00:00'))

