#i betterized it

class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        print "New Bike!!!"
        self.price = "$" + str(price)
        self.max_speed = str(max_speed) + "mph"
        self.miles = miles
    def displayinfo(self):
        print "Price is: " + self.price
        print "Maximum Speed is: " + self.max_speed
        print "Total Miles is: " + str(self.miles) + " miles"
    def ride(self):
        print "Riding"
        miles = self.miles
        self.miles += 10
    def reverse(self):
        print "Reversing"
        miles = self.miles
        if self.miles >= 5:
            self.miles -= 5

bike1 = Bike(200, 25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(100, 20)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3 = Bike(800, 30)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()
