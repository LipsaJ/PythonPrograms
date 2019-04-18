class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("wee.. I can fly!")
        elif self.ratio == 1:
            print("This is hard but I am trying")
        else:
            print("I'll just walk!")


class Duck:

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, Waddle, Waddle")

    def swim(self):
        print("I love swimming!")

    def quack(self):
        print("Quack!Quack!!")

    def fly(self):
        self._wing.fly()


class Penguin:

    def walk(self):
        print("Waddle, Waddle and I Waddle too")

    def swim(self):
        print("I love swimming but water is very cold")

    def quack(self):
        print("I dont quack!")


# def duck_test(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    # duck_test(donald)
    #
    # percy = Penguin()
    # duck_test(percy)

# so inheritance isn't class can behave in the same way as the only way to implement polymorphism a
# another class as long as it's got the class can behave in the same way as necessary methods and data attributes so

# inheritance "is a" relationship

# composition and aggression -- its based on "has a" relation ship
# for example duck "has a" wing
