class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name


john = Person("Johnathan", 12)
alice = Person("Alice",34)
khalid = Person("Khalid", 17.5)

people = [john, alice, khalid]

for person in people:
    if person.age >= 18:
        print(f"{person.name} can buy alcohol")
