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
        return self
    def ride(self):
        print "Riding"
        miles = self.miles
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        # miles = self.miles
        if self.miles >= 5:
            self.miles -= 5
        return self

bike1 = Bike(200, 25)
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = Bike(100, 20)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = Bike(800, 30)
bike3.reverse().reverse().reverse().displayinfo()
