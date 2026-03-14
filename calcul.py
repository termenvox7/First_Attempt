# Простой калькулятор на Python

def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    
    try:
        choice = input("Введите номер операции (1/2/3/4): ")
        
        if choice not in ['1', '2', '3', '4']:
            print("Ошибка: неверный выбор операции")
            return
        
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        
        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
    except ValueError:
        print("Ошибка: введите корректные числа")

if __name__ == "__main__":
    calculator()