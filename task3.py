# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Восстановить
# Ввёл: stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"

def create():                  # Считывает и записывает в файл введеное пользователем
    s = open("file.txt", "w+") #при отсутствии создаст файл  file.txt
    s.write(input())
    s.close()
create()

def create_cod():                 #записывает результат в файл file_cod.txt
    d = open("file_cod.txt", "w+")
    d.write(encoding)
    d.close()


with open('file.txt', 'r') as text:
        s = text.readline()
        
encoding = "" # сохраняет выходную строку
i = 0
while i < len(s):
        
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1 

    encoding += str(count) + s[i]# добавляет к результату текущий символ и его количество
    i = i + 1

create_cod() 
print(encoding)
 
with open('file_cod.txt', 'r') as text:
        cod = text.readline() # открыть и считать с файла  file_cod.txt

decod = ''
i = 0
j = 0
while (i <= len(cod) - 1):
    counts = int(cod[i])
    chars = cod[i + 1]
    for j in range(counts):
        decod += chars
        j += 1
    i += 2

print(decod)
           
    
 



