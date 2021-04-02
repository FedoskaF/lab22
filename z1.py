#!/usr/bin/env python3

import os

def remove_prefix(text, prefix): # функция для удаления префикса из названия файла
	return text[text.startswith(prefix) and len(prefix):]

# ввод данных

print('Enter a prefix')
prefix = input()

print('Enter the start of the file length range in bytes')
len_begin = input()

while len_begin.isdigit() == False:
    print('Please enter a positive integer')
    len_begin = input()

while int(len_begin) < 0:
    print('Please enter a positive integer')
    len_begin = input()

print('Enter the end of the file length range in bytes')
len_end = input()

while len_end.isdigit() == False:
    print('Please enter a positive integer')
    len_end = input()

while int(len_end) < 0:
    print('Please enter a positive integer')
    len_end = input()

if int(len_begin) > int(len_end): # если границы диапазона перепутаны местами, то просто поменяем их 
    len_begin, len_end = len_end, len_begin

list_of_files = [] # список удаляемых файлов

for adress, dirs, files in os.walk(os.getcwd()):
    for f in files:
        name = os.path.splitext(f)[0] # выделяем имя файла
        len_of_file = os.path.getsize(os.path.join(adress, f)) # определяем длину файла
        if len(f) >= len(prefix) and f != remove_prefix(f, prefix) and len_of_file >= int(len_begin) and len_of_file <= int(len_end):
            list_of_files.append(os.path.join(adress, f))

n = 0 # счётчик файлов

for f in list_of_files:
    os.remove(f) # удаляем все файлы, удовлетворяющие условиям
    n = n + 1

if n == 1:
    print(n, 'file was deleted')
else:
    print(n, 'files were deleted')
