a = 12
b = 6
print(a + b)  # it goes to same method as built in __add__
print(a.__add__(b))  # everything in python is an object
# when function is a part of an object its called a method
# when a variable is bound to an instance of a class then it's referred to as a data attribute


class Kettle(object):
    source_work = "electricity"  # this is class attribute

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


Liff = Kettle("Liffy", 600)
print(Liff.make)
print(Liff.price)

Liff.price = 840
print(Liff.price)

Hanzu = Kettle("Hanzu", 700)

print("Models: {} = {}, {} = {}".format(Liff.make, Liff.price, Hanzu.make, Hanzu.price))
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(Liff, Hanzu))

"""
Class: template
object: an instance
instantiate: create an instance of object
Method: a func defined in object
Attribute: a variable bound to an instance of a class
"""
print(Liff.on)
Liff.switch_on()
print(Liff.on)

Hanzu.power = 1.5
print(Hanzu)
print(Hanzu.power)
# print(Liff.power)  # this will throw an error

# two types of attributes data and method

print("set source to gas")
Kettle.source_work = "Gas"
print(Kettle.source_work)
print("Set Liff to atomic")
Liff.source_work = "atomic"  # after this change the Liff.__dict__ adds source_work to attribute, previously it used to
# only come with class i.e, Kettle.__dict__
print(Liff.source_work)
print(Hanzu.source_work)

print(Kettle.__dict__)
print(Liff.__dict__)
print(Hanzu.__dict__)
