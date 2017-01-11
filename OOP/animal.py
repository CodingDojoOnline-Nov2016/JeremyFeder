# Assignment: Animal
# MandatoryDeadline: Tuesday of Week 5Difficulty Level: AdvancedEstimated Time: 3-6 hrs
# Objective
# The objective of this assignment is to help you understand inheritance. Remember that a class is more than just a collection of properties and methods. If you want to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call. As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.
#
# To Do
# Create a class called Animal with the following attributes: name, and health. Give the animal following three methods: walk, run, and displayHealth. Give a new animal a health of 100 when it gets created. When a walk() method is invoked, have the health decrease by 1. When a run() method is invoked, have the health decrease by 5. When a displayHealth() method is invoked, display on screen the name of the Animal and the health.
#
# Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.
#
# Now, create another class called Dog that inherits everything that the Animal does and has, but 1) have the default health be 150 and 2) add a new method called pet, which when invoked, increase the health by 5. Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
#
# Now, create another class called Dragon that also inherits everything from Animal, but 1) have the default health be 170 and 2) add a new method called fly, which when invoked, decreased the health by 10. Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).
#
# Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:

# Create a class Animal

class Animal(object):
    def __init__(self, name):
        self.health = 100
        self.name = name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print 'Animal name is: ' + self.name
        print 'Health: ' + str(self.health)

animal = Animal('Harambe')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog = Dog('Lassie')
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon, self).displayHealth()

dragon = Dragon('Bruce Lee!')
dragon.fly().displayHealth()
