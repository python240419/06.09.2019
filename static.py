def my_print(msg):
    print(msg)

class Priner:
    def my_print(msg):
        print(msg)

class Circle():
    pi = 3.14
    area = 'pi * radius * radius'
    def __init__(self, radius):
        self.radius = radius
        #self.pi = 3.14
    def calcArea(self):
        return self.radius ** 2 * Circle.__pi
c = Circle(5.8)
print(c.calcArea())
#print(Circle.pi)
#Circle.pi = 4.5
print(c.calcArea())
# print(Circle.radius) # error

class Elipse(Circle):
    pass
Circle.pi = 9.9
Elipse.pi = 12.9

print(Circle.pi)
print(Elipse.pi)
