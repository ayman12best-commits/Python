# class parrot

class parrot:
    species = "maccaw"
    def __init__(self,name,age):
        self.name = name
        self.age = age


parrot1 = parrot("Blu",3)
parrot2 = parrot("Jolly",3)

print("The species of the parrot1 is : ",parrot1.species)
print("The name of the parrot1 is : ",parrot1.name)
print("The age of the parrot1 is : ",parrot1.age)

print("The species of the parrot2 is : ",parrot2.species)
print("The name of the parrot2 is : ",parrot2.name)
print("The age of the parrot2 is : ",parrot2.age)