# creating a simple model of a farm using animals and some actions that they take

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __str__(self):
        return f"\nAnimal: {self.name}\nSpecies:{self.species}"

    def make_sound(self):
        raise NotImplementedError("Method should be overridden by child classes")

    def move(self):
        raise NotImplementedError("Method should be overridden by child classes")

    def info(self):
        return f"{self.name} is a {self.species}"


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "Cow")

    def make_sound(self):
        return f"{self.name} says Moo!"

    def move(self):
        return f"{self.name} walks on 4 legs"


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "Chicken")


    def make_sound(self):
        return f"{self.name} says Cluck!"


    def move(self):
        return f"{self.name} walks on 2 legs & can flap its wings"


class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "Sheep")

    def make_sound(self):
        return f"{self.name} says Moo!"

    def move(self):
        return f"{self.name} walks on 4 legs & can sometimes run"


def main():
    # create animal instances
    cow = Cow("Jersey")
    chicken = Chicken("Clucky")
    sheep = Sheep("Bully")

    # create animal list
    animals = [cow, chicken, sheep]

    # show animal behaviors
    for elm in animals:
        print(elm.info())
        print(elm.make_sound())
        print(elm.move())
        print()


if __name__ == "__main__":
    main()
