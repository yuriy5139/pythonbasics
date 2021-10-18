from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name: str):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        print("дернули сеттер в Clothes")
        self.__name = name

    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def name(self, name):
        if name in ["Большевичка", "Большевик", "Борщевик"]:
            self.__name = name
        else:
            print("Ошибка! Список возможных марок пальто:", ["Большевичка", "Большевик", "Борщевик"])

    def calc_cloth(self):
        return self.size / 6.5 + 0.5


if __name__ == "__main__":
    question = "\n\nДобрый день :) \nПомогите разобраться, пожалуйста. Вот, что непонятно:\n" \
               "Видно, что в родительском классе сеттер не вызывается никогда - потому, что __init__ пишет напрямую в защищенный атрибут. \nВ " \
               "в дочернем классе сеттер переопределен. При этом наличие сеттера в дочернем классе, который пишет в защищенный(!) атрибут __name, \n" \
               "не меняет защищенный атрибут родительского класса (см принт выше - атрибут '_Clothes__name': 'Большевичка' остается неизменным),\n" \
               "но при этом он не создает и защищенный атрибут в дочернем классе (см. этот же принт  - атрибут 'name': 'Борщевик' - не защищен, нет dunder.)!\n\n" \
               "Также видно, что print((my_coat.__name)) выдает ошибку AttributeError: 'Coat' object has no attribute '__name'\n\n" \
               "Собственно, вопрос :) : Как же мне создать защищенный атрибут в классе Coat, воспользовавшись интерфейсом из Clothes?\n" \
               "То есть, я хочу объявить в родительском классе защищенный(!) атрибут __name, явно указать в интерфейсе,\n что к нему требуется сеттер (возможно, через @abstractmethod), который _должен_быть_" \
               "переопределен_ в дочернем классе\n в зависимости от логики класса. Как мне этого добиться? \n"

    my_coat = Coat("Большевичка", 65)
    my_coat.name = "Борщевик"
    print("\n")
    print(my_coat.__dict__)
    print(question)
    print((my_coat.__name))
