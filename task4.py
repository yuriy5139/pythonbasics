class Car():
    def __init__(self, color="черный", name="Жигули", is_police=False):
        self.speed = 0;
        self.color = color
        self.name = name
        self.is_police = is_police
        self._speed = 0

    def go(self, speed):
        self._speed = speed
        print("сообщение от {} {}: я поехала (вперед) со скоростью {}".format(self.color, self.name, speed))

    def stop(self):
        self._speed = 0
        print("сообщение от {} {}: а смысл куда-то вообще ехать?".format(self.color, self.name))

    def turn(self, dir):
        if self._speed:
            print("сообщение от {} {}: поворачиваю {}".format(self.color, self.name, dir))
        else:
            print("сообщение от {} {}: поворачиваю на месте :(".format(self.color, self.name))

    def show_speed(self):
        print("сообщение от {} {}: еду на скорости {}".format(self.color, self.name, self._speed))


class TownCar(Car):
    def __init__(self, color="белый", name="Хундай", is_police=False):
        super().__init__(color=color, name=name, is_police=is_police)

    def show_speed(self):
        print("сообщение от {} {}: еду на скорости {}".format(self.color, self.name, self._speed))
        if self._speed > 60:
            print("!Слишком быстро для TownCar!")


class WorkCar(Car):
    def __init__(self, color="желтый", name="Яндекскар", is_police=False):
        super().__init__(color=color, name=name, is_police=is_police)

    def show_speed(self):
        print("сообщение от {} {}: еду на скорости {}".format(self.color, self.name, self._speed))
        if self._speed > 40:
            print("!Слишком быстро для WorkCar!")


class SportCar(Car):
    def __init__(self, color="красный", name="Ягуар", is_police=False):
        super().__init__(color=color, name=name, is_police=is_police)


class PoliceCar(Car):
    def __init__(self, color="синий", name="УАЗ", is_police=True):
        super().__init__(color=color, name=name, is_police=is_police)


if __name__ == "__main__":
    townkar, workkar, sportkar, policekar = TownCar(), WorkCar(), SportCar(), PoliceCar()

    workkar.go(50)
    townkar.go(70)
    workkar.show_speed()
    townkar.show_speed()
    workkar.turn("направо")
    townkar.stop()
    townkar.turn('налево')
