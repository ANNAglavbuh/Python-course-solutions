"""
3.1.2 Задача 2: Среднее по списку

Создайте список случайных значений и найдите для него: среднее,
дисперсию и медиану.
Выведите список этих чисел и полученные значения.
"""
# -*- coding: utf-8 -*-

import random
import statistics  # модуль для вычисления среднего, медианы, дисперсии

#!/usr/bin/env python3 import random import statistics

#Создаем список из 10 случайных целых чисел от 0 до 100
random_numbers = [random.randint(0, 100) for _ in range(10)]

#Вычисляем среднее значение
mean_value = statistics.mean(random_numbers)

#Вычисляем дисперсию
variance_value = statistics.variance(random_numbers)

#Вычисляем медиану
median_value = statistics.median(random_numbers)

#Вывод списка и полученных значений
print("Список случайных чисел:", random_numbers)
print("Среднее значение:", mean_value)
print("Дисперсия:", variance_value)
print("Медиана:", median_value)

