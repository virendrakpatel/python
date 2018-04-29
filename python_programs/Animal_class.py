__name__= 'Virendra Patel'

class Dog(object):

    species =  'mammal'

    def __init__(self, breed, name, fur = True):

        self.breed = breed
        self.name = name
        self.fur = fur

    def bark(self):
        print("Bho")

s= Dog(breed='Huskie', name='Sammy', fur= False)
print(s.name)

s.bark()

class Animal(object):

    def __init__(self):
        print ("Animal created")

    def whoami(self, name, age):
        print("Animal")
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)

    def eat(self):
        print("Eating")

class Dog(Animal):
    try:
        def __init__(self):
            Animal.__init__(Animal)
            print("Dog Created")
        def whoami(self, name):
            try:
                print("Dog")
                self.name = name
                print(self.name)
            except:
                print("I'm in exception")
            finally:
                print("I'm in Dog:whoami:Finally")
        def bark(self):
            print("woof")
    except:
        print("I'm in exception")
    finally:
        print("I'm in Dog:Finally")

a = Animal()
d = Dog()
print("------------------")
# a.whoami("Sammy",49)
d.whoami("Sammy")
# d.whoami("Sammy",49)
d.eat()

