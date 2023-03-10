colors = list()     #  List colors = new List();

colors.append('blue')
colors.append('green')

class Dog:
    def bark(self):
        print("Woof! woof!")

d1 = Dog()
d2 = Dog()
d1.bark()  # instance method
d2.bark()
print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"Dog: {Dog}")
