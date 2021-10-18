from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str):
        self.__name = name

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, name="Большевичка", size=48):
        super().__init__(name)
        self.size = size

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in ["Большевичка", "Большевик", "Борщевик"]:
            self.__name = name
        else:
            print("Ошибка! Список возможных марок пальто:", ["Большевичка", "Большевик", "Борщевик"])

    @property
    def cloth(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name="Большевик", height=170):
        super().__init__(name)
        self.height = height

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in ["Большевичка", "Большевик", "Борщевик"]:
            self.__name = name
        else:
            print("Ошибка! Список возможных марок костюмов:", ["Большевичка", "Большевик", "Борщевик"])

    @property
    def cloth(self):
        return self.height * 2 + 0.3


if __name__ == "__main__":
    my_coat = Coat(size = 65)
    my_suit = Suit(height = 180)
    my_coat.name = "Большевик"
    my_suit.name = "Hugo Boss"
    my_suit.name = "Борщевик"
    print("На пошив пальто {} требуется {:.3f} квадратных метров ткани".format(my_coat.name, my_coat.cloth))
    print("На пошив костюма {} требуется {:.3f} квадратных дюймов ткани".format(my_suit.name, my_suit.cloth))


