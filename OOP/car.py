class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax=0.12):
        print "New Car"
        self.price = price
        self.speed = str(speed) + "mph"
        self.fuel = str(fuel)
        self.mileage = str(mileage) + "mpg"
        self.tax = tax
        self.display_all()

    def display_all(self):
        if self.price > 10000:
            self.tax = 0.15
        print "Price: " + "$" + str(self.price)
        print "Speed: " + self.speed
        print "Fuel: " + self.fuel
        print "Mileage: " + self.mileage
        print "Tax: " + str(self.tax)

car1 = Car(9000, 140, "Full", 15)
car2 = Car(15000, 120, "Empty", 14)
car3 = Car(2000, 130, "Half-Full", 25)
car4 = Car(25000, 190, "Full", 8)
car5 = Car(12000, 110, "Full", 28)
car6 = Car(10000, 150, "Full", 12)
