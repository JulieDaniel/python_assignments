class product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        return self.price + (tax * self.price)

    def p_return(self, reason, box_condition):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        if box_condition == "unopened":
            self.status = "for sale"
        if box_condition == "opened":
            self.status = "used"
            self.price = self.price *.8
        return self

    def display_info(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status
        return self

product1= product(4.59, "socks", "1oz", "Cozy")

product1.display_info()
product1.sell()
product1.p_return("don't like", "unopened")
product1.sell()
product1.p_return("too much money", "opened")
product1.display_info()