from Car import Car

class Cars(list):
    def add(self, car):
        self.append(car)
    def find(self, car_id):
        for i in self:
            if i.car_id == car_id:
                return i
        # return next(x for x in self if x.car_id == car_id)

car_data = [
    {
        'car_id': 'B AB 4067',
        'brand': 'VW',
        'name': 'Golf 5',
        'seats': 4,
        'color': 'black',
        'price': 0.50
    },
    {
        'car_id': 'B RAS 667',
        'brand': 'Audi',
        'name': 'A5',
        'seats': 4,
        'color': 'grey',
        'price': 0.70
    },
    {
        'car_id': 'B ENG 5689',
        'brand': 'VW',
        'name': 'Passat',
        'seats': 4,
        'color': 'blue',
        'price': 0.65
    }
    ,
    {
        'car_id': 'B HF 6903',
        'brand': 'Renault',
        'name': 'Zoe',
        'seats': 4,
        'color': 'white',
        'price': 0.40
    }
    ,
    {
        'car_id': 'B RF 490',
        'brand': 'Mazda',
        'name': '3',
        'seats': 4,
        'color': 'red',
        'price': 0.50
    }
]

cars = Cars()
for i in car_data:
    car = Car(i['car_id'], i['brand'], i['name'], i['seats'], i['color'], i['price'])
    cars.add(car)



