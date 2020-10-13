from Address import Address

class Customer():
    def __init__(self, customer_id, name, street, number, city, zip, country, age, license_id):
        self.customer_id = customer_id
        self.name = name
        self.address = Address(street, number, city, zip, country)
        self.age = age
        self.license_id = license_id

customer_data = [
    {
        'customer_id': 1,
        'name': 'Frank Weider',
        'street': 'Weinmarstr.',
        'number': 46,
        'city': 'Berlin',
        'country': 'Germany',
        'zip': 12345,
        'age': 24,
        'license_id': 'B66002OKT01'
    },
    {
        'customer_id': 2,
        'name': 'Heinz Meiler',
        'street': 'Karl-Lange Str..',
        'number': 21,
        'city': 'Berlin',
        'country': 'Germany',
        'zip': 11002,
        'age': 35,
        'license_id': 'B7902OER01'
    },
    {
        'customer_id': 3,
        'name': 'Thomas Mannheimer',
        'street': 'Große Allee',
        'number': 3,
        'city': 'Berlin',
        'country': 'Germany',
        'zip': 11309,
        'age': 30,
        'license_id': 'B78060IU78'
    },
    {
        'customer_id': 4,
        'name': 'Anja Meier',
        'street': 'Grüne Ecke',
        'number': 90,
        'city': 'Berlin',
        'country': 'Germany',
        'zip': 10045,
        'age': 19,
        'license_id': 'A47949JU02'
    },
    {
        'customer_id': 5,
        'name': 'Margaret Daimer',
        'street': 'Pfauenweg',
        'number': 14,
        'city': 'Berlin',
        'country': 'Germany',
        'zip': 10078,
        'age': 30,
        'license_id': 'A00782RT34'
    }
]

for i in customer_data:
    customer = Customer(i['customer_id'], i['name'], i['street'], i['number'], i['city'], i['zip'], i['country'], i['age'], i['license_id'])
