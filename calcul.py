#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Инженерный калькулятор "Валерик" синего цвета
"""

import math
import sys

# Коды цветов ANSI
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_blue(text):
    """Вывод текста синим цветом"""
    print(f"{BLUE}{text}{RESET}")

def print_green(text):
    """Вывод текста зелёным цветом"""
    print(f"{GREEN}{text}{RESET}")

def print_red(text):
    """Вывод текста красным цветом (для ошибок)"""
    print(f"{RED}{text}{RESET}")

def show_menu():
    """Отображение меню"""
    print_blue("\n" + "="*50)
    print_blue(f"{BOLD}ИНЖЕНЕРНЫЙ КАЛЬКУЛЯТОР 'ВАЛЕРИК'🔵{RESET}")
    print_blue("="*50)
    print_blue("Выберите операцию:")
    print_blue(" 1. Сложение           (+)")
    print_blue(" 2. Вычитание          (-)")
    print_blue(" 3. Умножение          (*)")
    print_blue(" 4. Деление            (/)")
    print_blue(" 5. Возведение в степень (^)")
    print_blue(" 6. Квадратный корень   (√)")
    print_blue(" 7. Синус              (sin)")
    print_blue(" 8. Косинус            (cos)")
    print_blue(" 9. Тангенс            (tan)")
    print_blue("10. Логарифм натуральный (ln)")
    print_blue("11. Логарифм по основанию 10 (log10)")
    print_blue(" 0. Выход")
    print_blue("-"*50)

def get_number(prompt):
    """Ввод числа с обработкой ошибок"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print_red("Ошибка: введите число!")

def main():
    while True:
        show_menu()
        choice = input(f"{CYAN}Введите номер операции: {RESET}").strip()
        
        if choice == '0':
            print_green("До свидания, Валерик выключается... 👋")
            break
        
        # Операции с двумя аргументами
        if choice in ['1', '2', '3', '4', '5']:
            a = get_number("Введите первое число: ")
            b = get_number("Введите второе число: ")
            
            if choice == '1':
                result = a + b
                print_green(f"{a} + {b} = {result}")
            elif choice == '2':
                result = a - b
                print_green(f"{a} - {b} = {result}")
            elif choice == '3':
                result = a * b
                print_green(f"{a} * {b} = {result}")
            elif choice == '4':
                if b == 0:
                    print_red("Ошибка: деление на ноль!")
                else:
                    result = a / b
                    print_green(f"{a} / {b} = {result}")
            elif choice == '5':
                result = a ** b
                print_green(f"{a} ^ {b} = {result}")
        
        # Операции с одним аргументом
        elif choice in ['6', '7', '8', '9', '10', '11']:
            a = get_number("Введите число: ")
            
            if choice == '6':
                if a < 0:
                    print_red("Ошибка: корень из отрицательного числа!")
                else:
                    result = math.sqrt(a)
                    print_green(f"√{a} = {result}")
            elif choice == '7':
                result = math.sin(a)
                print_green(f"sin({a}) = {result}")
            elif choice == '8':
                result = math.cos(a)
                print_green(f"cos({a}) = {result}")
            elif choice == '9':
                result = math.tan(a)
                print_green(f"tan({a}) = {result}")
            elif choice == '10':
                if a <= 0:
                    print_red("Ошибка: логарифм из неположительного числа!")
                else:
                    result = math.log(a)
                    print_green(f"ln({a}) = {result}")
            elif choice == '11':
                if a <= 0:
                    print_red("Ошибка: логарифм из неположительного числа!")
                else:
                    result = math.log10(a)
                    print_green(f"log10({a}) = {result}")
        else:
            print_red("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
