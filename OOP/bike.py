class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        print "New Bike!!!"
        self.price = "$" + str(price)
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        price = self.price
        max_speed = self.max_speed
        miles = self.miles
        print price
        print max_speed
        print miles
    def ride(self):
        print "Riding"
        miles = self.miles
        self.miles += 10
    def reverse(self):
        print "Reversing"
        miles = self.miles
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(200, "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(100, "20mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3 = Bike(800, "30mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()
