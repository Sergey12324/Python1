name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = int(input("Введите ваш возраст: "))

# Вывод через метод format()
print("\nРеализация через format:")
print("Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age))

# Вывод через f-string
print("\nРеализация через f-string:")
print(f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет")

input("\nНажмите Enter для выхода...")