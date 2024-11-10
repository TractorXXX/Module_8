def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    n = -1

    for i in numbers:
        try:
            n += 1
            result += numbers[n]
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы -',i)
            incorrect_data += 1

    a = (result, incorrect_data)
    return a


def calculate_average(numbers):
    try:
        tuple_funk = personal_sum(numbers)
        kol_vo = len(numbers) - tuple_funk[1]
        sr_arifmet = tuple_funk[0] / kol_vo
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
    else:
        return sr_arifmet


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
