# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 22:57:00 2021

@author: Ya
"""

my_str = input("Пожалуйста, введите несколько слов разделяя их пробелами: ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1
        