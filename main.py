"""
Написать программу, которая:
- Создаёт случайный список из 20 значений по 4 случайных целых чисел от -10 до 10.
- Находит все уникальные комбинации пар из этих значений и выводит их в виде списка кортежей.
- Пользователь вводит целое число.
- Вычисляет количество пар, чья сумма меньше заданного пользователем значения.
"""

import random #подключение модуля random

s = [] #создание пустого основного списка
for i in range(20): #цикл для создания 20 значений
    x = [random.randint(-10, 10) for a in range(4)] #создание списка из 4 случайных чисел от -10 до 10
    s.append(x) #добавление созданного списка в основной

u_pairs = [] #создание пустого списка для уникальных пар
for i in range(len(s)): # цикл, где проходит по каждому элементу основного списка
    for j in range(i + 1, len(s)): #цикл для создания уникальных пар значений без повторения
        pair = (s[i], s[j]) #создание пары
        u_pairs.append(pair) #добавление пар в список для уникальных пар
print("Уникальные комбинации пар:", u_pairs) #вывод уникальных комбинаций пар

user_value = int(input("Введите целое число: ")) #ввод целого числа

count = 0 #счетчик количества пар
for pair in u_pairs: #цик, где проходит по каждой паре
    if sum(pair[0]) + sum(pair[1]) < user_value: #если сумма элементов пары меньше числа
        count += 1 #работа счетчика
print(f"Количество пар, чья сумма меньше заданного числа :", count) #вывод
