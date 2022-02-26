

# Создайте класс Person у которого будет один единственный метод use_transport.
# В данный метод в качестве параметра должен передаваться объект реализующий интерфейс Transport
# Метод для этого объекта должен запускать двигатель, двигаться куда-то, тормозить и глушить двигатель.
# Для текстовой анимации Вы можете использовать любые фразы, или воспользоваться нашей подборкой:
# Boat:
#    - Катер громко затарахтел
#    - Двигатель катера чихнул напоследок и заглох
#    - Катер быстро набирает скорость
#    - Катер остановился
# Car:
#    - Машина заурчала двигателем
#    - Машина стоит с заглушенным двигателем
#    - Машина едет к цели назначения
#    - Машина остановилась
# Electroscooter:
#    - Мигнул светодиодом
#    - Мигнул светодиодом дважды
#    - Прохожие в ужасе разбегаются от очередного камикадзе
#    - Торможение об стену прошло успешно


from abc import ABC, abstractmethod


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):

    def start_engine(self):
        print('Двигатель катера запущен')

    def stop_engine(self):
        print('Двигатель катера остановлен')

    def move(self):
        print('Катер несется')

    def stop(self):
        print('Катер остановился')


class Car(Transport):

    def start_engine(self):
        print('Двигатель машины запущен')

    def stop_engine(self):
        print('Двигатель машины остановлен')

    def move(self):
        print('Машина перемещается')

    def stop(self):
        print('Машина тормозит')


class Electroscooter(Transport):

    def start_engine(self):
        print('Двигатель электроскутера запущен')

    def stop_engine(self):
        print('Двигатель электроскутера остановлен')

    def move(self):
        print('Электроскутер мчится')

    def stop(self):
        print('Электроскутер тормозит')


class Person:
    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.stop_engine()
        transport.move()
        transport.stop()



# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
