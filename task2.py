def yellowpage(name="", lname="", birth='', city="", email="", phone=""):
    """Выводит информацию о пользователе

    name - имя пользователя
    lname - фамилия пользователя
    birth - год рождения
    city - город проживания
    email - адрес почты
    phone - номер телефона

    """

    print(f"Пользователь {name} {lname} {birth} г.р. проживает в г. {city}. Email: {email}, Тел.: {phone}")


yellowpage(name="Кентукки", lname="Фрайдчиккен", birth=1952, city="Луисвилл, США", email="info@kfc.com",
           phone="+1-234-567-8901")
