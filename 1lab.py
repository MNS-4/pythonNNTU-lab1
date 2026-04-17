# Перевод десятичного числа в заданную систему счисления (основание от 2 до 9)
# Число и основание вводятся с клавиатуры.


# Ввод числа с проверкой корректности
while True:
    try:
        number = int(input("Введите целое число: "))
        break
    except ValueError:
        print("Это не число, попробуйте снова.")
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван.")
        exit()

# Ввод основания системы счисления с проверкой корректности
while True:
    try:
        base = int(input("Введите систему счисления (2-9): "))
        if base < 2 or base > 9:
            print("Ошибка: основание должно быть от 2 до 9.")
        else:
            break
    except ValueError:
        print("Это не число, попробуйте снова.")
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван.")
        exit()

# Перевод числа в заданную систему счисления
if number == 0:
    result = "0"
else:
    result = ""
    n = abs(number)
    # Берём остатки от деления и собираем цифры
    while n > 0:
        result = str(n % base) + result
        n //= base
    # Если число отрицательное — добавляем минус
    if number < 0:
        result = "-" + result

# Вывод результата
print("\n--- Результат ---")
print(f"Число {number} в системе счисления {base} = {result}")