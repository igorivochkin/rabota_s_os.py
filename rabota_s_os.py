#rabota_s_os.py
import os
import time

'''print('Текущая директория', os.getcwd())
print(os.times())
if os.path.exists('new_dir'):
    os.chdir('new_dir')
else:
    os.mkdir('new_dir')# Создать директорию
    os.chdir('new_dir')# установить директорию
print('Текущая директория', os.getcwd())
print(os.listdir())'''

print('Текущая директория', os.getcwd())
directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


