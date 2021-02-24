class Swift:
    def drive(self):
        print("driving swift car")

class Sonet:
    def drive(self):
        print("driving sonet")

class Person:
    def start(self,car):
        car.drive()

sw = Swift()
p = Person()
p.start(sw)

