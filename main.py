"""На языке Питон написать программу, которая из файла читает объекты, разделенные  пробелами,
выводит их на экран, производит заданную обработку и  результат выводит на экран.
Обработка: через регулярные выражения найти сумму и количество натуральных четных пятиразрядных десятичных чисел,
в которых первая цифра равна 2, из которых определить максимальное число и их количество."""

import re
def _regular(filename):
    with open(filename, 'r') as file:
        data = file.read()

    pattern = r'\b2\d{4}\b'
    matches = re.findall(pattern, data)

    numbers = [int(num) for num in matches if int(num) % 2 == 0 and int(num) > 0]

    _sum = sum(numbers)
    count = len(numbers)

    if numbers:
        max_number = max(numbers)
        max_count = numbers.count(max_number)
    else:
        max_number = None
        max_count = 0

    return _sum, count, max_number, max_count

def main():
    filename = 'ekzamen.txt'
    total_sum, count, max_number, max_count = _regular(filename)

    print("Сумма натуральных четных пятиразрядных чисел с первой цифрой 2:", total_sum)
    print("Колво найденных чисел:", count)
    if max_number is not None:
        print("Макс число:", max_number)
        print("Колво макс чисел:", max_count)
    else:
        print("Ни одного подходящего числа не найдено.")

if __name__ == "__main__":
    main()
