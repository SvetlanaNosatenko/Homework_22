# Измените класс Person так, чтобы его методы
# оперировали внутренним состоянием,
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, person_room, population):
        self.person_room = person_room
        self.population = population

    def get_person_room(self):
        return self.person_room

    def get_city_population(self):
        return self.population


person_1 = Person(10, 100500)
print(person_1.get_person_room())
print(person_1.get_city_population())
# сделать экземпляр класса person и вызвать новые методы.