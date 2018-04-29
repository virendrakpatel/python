
class Dog(object):
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # def cat(self, breed, name):
    #     self.breed = breed
    #     self.name = name

sam = Dog(breed = "Husky", name = 'Sammy')

print(sam.breed)
print(sam.name)
print(sam.species)


class Circle(object):
    '''
    class objects attributes
    '''
    pi = 3.14
    pass

    def __init__(self, radius = 1):
        self.radius = radius
        # self.perimiter = perimiter
        pass

    def area(self):
        # radius ** 2 * pi
        return (self.radius**2) * self.pi

    def set_radius(self, new_radius):
        self.radius = new_radius
        """
        this method takes in a radius, and reset the current radius of the Circle.
        :param new_radius:
        :return:
        """

    def get_radius(self):
        return self.radius

    def perimiter(self):
        return (self.radius*2) * self.pi

print("----------------------------------------------------")
c = Circle(radius=10)
print(c.radius)
print(c.pi)
print(c.area())

print("----------------------------------------------------")
c.set_radius(new_radius=20)
print(c.radius)
print(c.pi)
print(c.area())

print("----------------------------------------------------")
print(c.get_radius())
print(c.perimiter())


