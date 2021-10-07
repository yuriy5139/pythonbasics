import sys
import random

def calc_wage(hours = 0, per_h = 0, bonus = 0):
    return hours*per_h + bonus

if __name__ == "__main__":
    try:
        print("Заработная плата составляет {} руб.".format(calc_wage(hours = int(sys.argv[1]), per_h = int(sys.argv[2]),
                                       bonus = int(sys.argv[3]))))
    except:
        print("Скрипт должен содержать три параметра int - количество отработанных часов, стоимость часа и бонус.")
    finally:
        print("Как поработал - так и заработал {}".format(random.choice([":)", ":("])))