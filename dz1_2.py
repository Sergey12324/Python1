number = input("Введите число: ").strip()

try:
    n = int(number)
    if n <= 0:
        print("Ошибка: введено не положительное число")
    else:
        if n % 2 == 0:
            print(f"Число {n} является четным")
        else:
            print(f"Число {n} не является четным")
except ValueError:
    print("Ошибка: введено не число")