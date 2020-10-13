from Booking import Booking
import Cars

import time
import datetime
get_datetime = lambda date_time_str: datetime.datetime.strptime(date_time_str, '%d.%m.%Y %H:%M:%S')

class Car_bookings(list):
    def __init__(self, cars):
        self.cars = cars
        self.counter = 0
    def book(self, customer_id, car_id, begin, end):
        car = self.cars.find(car_id)
        if (car.available):
            booking = Booking(self.counter, customer_id, car, begin, end)
            self.counter = self.counter+1
            self.cars.find(car_id).available = False
            self.append(booking)
            print()
            print('Booked for {}, car is no longer available from {} to {} with the booking-Id: {}'.format(car_id, begin, end, self.counter))
            print('Available cars:')
            for i in self.cars:
                print(i)
        else:
            print(car.car_id + " isn't available")
    def unbook(self, car_id):
        self.cars.find(car_id).available = True
        print()
        print('Car {} has been unbooked and is available again'.format(car_id))
        print('Available cars:')
        for i in self.cars:
            print(i)


car_bookings = Car_bookings(Cars.cars)
car_bookings.book(1, 'B HF 6903', '12.10.2020 12:00:00', '18.10.2020 18:00:00')
car_bookings.book(1, 'B HF 6903', '12.10.2020 12:00:00', '18.10.2020 18:00:00')
car_bookings.book(4, 'B ENG 5689', '14.10.2020 16:30:00', '15.10.2020 12:00:00')
time.sleep(5)
car_bookings.unbook('B HF 6903')

