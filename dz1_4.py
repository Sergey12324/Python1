while True:
    user_input = input("Введите число: ").strip()

    if user_input.lower() == 'exit':
        print("Выход из программы...")
        break

    if not user_input:
        print("Ошибка: пустой ввод.")
        continue

    cleaned = user_input.lstrip('-')

    if cleaned.isdigit() and cleaned != '':
        print(f"В этом числе {len(cleaned)} цифры.")
    else:
        print("Ошибка: данные не являются числом.")