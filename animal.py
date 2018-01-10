class animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
         self.health -= 1

    def run(self):
        self.health -= 5

    def display_health(self):
        msg = "Animal's name is " + self.name + ". It's health is " + str(self.health)
        print msg

class dog(animal):
    def __init__(self, name, health = 150):
        animal.__init__(self, name, health)

    def pet(self):
        self.health += 5

class dragon(animal):
    def __init__(self, name, health = 170):
        animal.__init__(self, name, health)

    def fly(self):
        self.fly += 10

    def display_health(self):
        animal.display_health(self)
        print "I'm a dragon"



animal1 = animal("Comet", 50)

animal1.walk()
animal1.walk()
animal1.walk()
animal1.run()
animal1.run()
animal1.display_health()

dog1 = dog("Kiddo")

dog1.walk()
dog1.walk()
dog1.walk()
dog1.run()
dog1.run()
dog1.pet()
dog1.display_health()

dragon1 = dragon("Flame")
dragon1.display_health()

animal2 = animal("Cotton",122)
# animal2.pet()
animal2.display_health()
# animal2.fly()

# dog1.fly()