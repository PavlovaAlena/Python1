# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным
import os 
os.system('cls')

print("Программа проверяет цифру на соответствие дня недели выходному дню")
digitDay = int(input("Введите цифру дня недели: "))

# Первое решение задачи
if digitDay > 0 and digitDay < 8:

    if digitDay < 6:
        print(
            f"Цифре {digitDay} не соответствует выходной день, это будний день")
    else:
        print(f"Цифре {digitDay} соответствует выходной день")
else:
    print(f"Цифре {digitDay} нет соответствия дня недели")


""" # Второе решение задачи
match digitDay:
    case 1 | 2 | 3 | 4 | 5:
        print(
            f"Цифре {digitDay} не соответствует выходной день, это будний день")
    case 6 | 7:
        print(f"Цифре {digitDay} соответствует выходной день")
    case _:
        print(f"Цифре {digitDay} нет соответствия дня недели")
 """