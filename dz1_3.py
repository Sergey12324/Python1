age_input = input("Введите ваш возраст: ").strip()

try:
    age = int(age_input)

    if age <= 0:
        print("Ошибка: возраст должен быть положительным числом.")
    else:
        if age >= 18:
            print("Вы совершеннолетний.")
        else:
            print("Вы несовершеннолетний.")

except ValueError:
    print("Ошибка: введено не число!")