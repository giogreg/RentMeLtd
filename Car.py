class Car():
    def __init__(self, car_id, brand, name, seats, color, price):
        self.car_id = car_id
        self.brand = brand
        self.name = name
        self.seats = seats
        self.color = color
        self.price = price
        self.available = True
    def __str__(self):
        return "{} {} {} {}-seater {} {} euro Available: {}".format(self.car_id, self.brand, self.name, self.seats, self.color, self.price, self.available)

