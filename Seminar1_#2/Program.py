# Задача 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
import os 
os.system('cls')

print("Программа проверяет истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.")
x = (input(f"Введите значение x: "))
y = (input(f"Введите значение y: "))
z = (input(f"Введите значение z: "))

left = not (x or y or z)
right = not x and not y and not z

if left == right:
    print(f"Утверждение ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} истинно")
else:
    print(f"Утверждение ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} ложно")
