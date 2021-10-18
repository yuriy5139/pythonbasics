from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, name="Большевичка", size=48):
        super().__init__(name)
        self.size = size

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if name in ["Большевичка", "Большевик", "Борщевик"]:
            self.name = name
        else:
            print("Ошибка! Список возможных марок пальто:", ["Большевичка", "Большевик", "Борщевик"])

    @property
    def cloth(self):
        return self.size / 6.5 + 0.5

if __name__ == "__main__":
    question2 = "\nЕще раз добрый день :)\nПодскажите, пожалуйста, если раскомментировать строку создания объекта my_coat ниже, \n" \
                "система попадает в бесконечную рекурсию - почему? "
    print(question2)
    # my_coat = Coat()


