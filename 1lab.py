# Количество положительных чисел, отрицательных и равных нулю
# Список чисел вводится с клавиатуры.


# Ввод количества чисел с проверкой что это число 
while True:
    try:
        n = int(input("Введите количество чисел: "))
        if n < 0:
            print("Количество чисел не может быть отрицательным.")
        else:
            break
    except ValueError:
        print("Ошибка: введите целое число.")
    except (EOFError, KeyboardInterrupt):
        print("\nВвод прерван")
        exit()

# Счетчики 
positive = 0
negative = 0
zero = 0

# Проверка что это число + определение знака числа
for i in range(n):
    while True:
        try:
            num = int(input("Введите целое число: "))
            break
        except ValueError:
            print("Это не число, попробуйте снова")
        except (EOFError, KeyboardInterrupt):
            print("\nВвод прерван")
            exit()

    # Проверка числа
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

# Вывод результатов
print("\n--- Результаты ---")
print("Положительных чисел:", positive)
print("Отрицательных чисел:", negative)
print("Чисел равных нулю:", zero)