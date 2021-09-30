month = int(input("введите номер месяца от 1 до 12 "))

print("Решение через list")
winter = [12, 1, 2, "зима"]
spring = [3, 4, 5, "весна"]
summer = [6, 7, 8, "лето"]
autumn = [9, 10, 11, "осень"]

for season in [winter, spring, summer, autumn]:
    if month in season:
        print(f"Месяц {month}  - это {season[3]}")
        break

print("Решение через dict")
year = {1: "зима", 2: "вообще зима", 3: "еще зима", 4: "почти весна", 5: "весна", 6: "лето", 7: "лето", 8: " ну как лето",
          9: "осень", 10: "совсем осень", 11: "не спрашивайте", 12: "зима"}
print(f"Месяц {month}  - это {year[month]}")