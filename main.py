"""
Лабораторная работа №1.
Вариант 4
Беляев Антон
ИСУ: 465204
"""

import os
import time
import math


# Флаг
def print_flag():
    print("Флаг Польши:\n")
    for _ in range(5):
        print("████████████████████")  # белая часть
    for _ in range(5):
        print("####################")  # красная часть
    print("\n")


# Узор 
def print_pattern():
    print("Узор d:\n")
    for i in range(6):
        if i % 2 == 0:
            print("==========")
        else:
            print("  ||  ")
    print("\n")


# График
def print_function_graph():
    print("График функции y = sqrt(x):\n")
    for x in range(9):
        y = int(math.sqrt(x) * 3)
        print(" " * y + "*")
    print("\n")


# sequence.txt
def process_sequence():
    print("Обработка sequence.txt:\n")
    
    try:
        with open("sequence.txt", "r") as f:
            numbers = list(map(float, f.read().split()))
        
        if len(numbers) < 250:
            print("В файле должно быть минимум 250 чисел!\n")
            return
        
        first_125 = numbers[:125]
        second_125 = numbers[125:250]
        
        avg1 = sum(abs(x) for x in first_125) / 125
        avg2 = sum(abs(x) for x in second_125) / 125
        
        total = avg1 + avg2
        percent1 = avg1 / total * 100
        percent2 = avg2 / total * 100
        
        print(f"Среднее первых 125: {avg1:.2f}")
        print(f"Среднее вторых 125: {avg2:.2f}")
        print(f"Процентное соотношение:")
        print(f"Первая часть: {percent1:.2f}%")
        print(f"Вторая часть: {percent2:.2f}%\n")
        
    except FileNotFoundError:
        print("Файл sequence.txt не найден!\n")


# Анимация
def animation():
    print("Анимация завершена")
    


def main():
    print_flag()
    print_pattern()
    print_function_graph()
    process_sequence()
    animation()


if __name__ == "__main__":
    main()