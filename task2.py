class Road():
    def __init__(self, length=1, width=1):
        self._length = length
        self._width = width

    def calc(self, layer):
        return self._width * self._length * 25 * layer


if __name__ == "__main__":
    length = 20
    width = 5000
    layer = 5
    r = Road(length, width)
    print("Чтобы покрыть дорогу длиной {}м и шириной {}м асфальтом толщиной {}см, требуется {:,}кг асфальта".format(
        length, width, layer, r.calc(layer)
    ))
