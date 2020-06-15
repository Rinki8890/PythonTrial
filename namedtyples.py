from collections import namedtuple
Car = namedtuple('Car','Price Mileage Colour Class')
xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
print (xyz)
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print (xyz.Class)
