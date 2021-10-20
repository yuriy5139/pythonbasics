class MyDate:
    def __init__(self, datestr="", d=None, m=None, y=None):
        self.datestr = datestr
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def cretate_date(cls, datestr):
        if cls.is_date_valid(datestr):
            d, m, y = map(int, datestr.split("-"))
            return cls(datestr="", d=d, m=m, y=y)

    @staticmethod
    def is_date_valid(datestr):
        try:
            d, m, y = map(int, datestr.split("-"))
            if 1 > d or d > 31:
                return False
            else:
                return True
        except Exception as e:
            print("снова что-то пошло не так:", e)


if __name__ == "__main__":
    date1 = MyDate("01-01-2021")
    date2 = MyDate.cretate_date("02-02-2022")
    print(vars(date1))
    print(vars(date2))
