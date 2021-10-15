import time
import threading


class TrafficLight():
    def __init__(self):
        self.__running = False
        self.__color = "R"
        self.__direction = "toGreen"

    def run(self):
        while True:
            if self.__running:
                if self.__color == "R":
                    print("красный")
                    self.__color = "Y"
                    self.__direction = "toGreen"
                    time.sleep(7)
                if self.__color == "Y":
                    print("желтый")
                    if self.__direction == "toGreen":
                        self.__color = "G"
                        self.__direction = "toRed"
                    else:
                        self.__color = "R"
                        self.__direction = "toGreen"
                    time.sleep(2)
                if self.__color == "G":
                    print("зеленый")
                    self.__color = "Y"
                    self.__direction = "toRed"
                    time.sleep(7)
            else:
                print("остановил")
                return

    def start(self):
        time.sleep(2)
        if not self.__running:
            print("запускаем...")
            time.sleep(1)
            self.__running = True
            self.run()
        else:
            print("уже работает")

    def stop(self):
        print("останавливаем..")
        self.__running = False

    def switch(self, color):
        print("переключили на", color)
        self.__color = color
        if color == "R":
            self.__direction = "toGreen"
        else:
            self.__direction = "toRed"


def runthelight(tl_list):
    tl = TrafficLight()
    tl_list.append(tl)
    tl.start()


if __name__ == "__main__":
    tl_list = []
    x = threading.Thread(target=runthelight, args=(tl_list,), daemon=True)
    x.start()
    while True:
        command = input("введите команду: R, G, Y или S - (Stop)\n")
        if command != "S":
            tl_list[0].switch(command)
        else:
            tl_list[0].stop()
            break
    x.join()
