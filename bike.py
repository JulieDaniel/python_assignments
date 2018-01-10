class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "Price:", self.price
        print "Max speed:", self.max_speed
        print "Miles:",  self.miles
        return self


    def ride(self):
        print "Riding"
        self.miles+=10
        return self

    def reverse(self):
        print "Reversing"
        self.miles-=5
        if self.miles < 0:
            self.miles = 0
        return self


bike1 = bike(200, "25mph")

bike2 = bike(300, "30mph")

bike3 = bike(400, "35mph")


bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()


bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()


bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()


