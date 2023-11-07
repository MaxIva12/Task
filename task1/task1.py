import sys

# считываем параметры командной строки
n = int(sys.argv[1])
m = int(sys.argv[2])

# формируем круговой массив
circle_array = list(range(1, n+1))


current_index = (m - 1) % n

# формируем путь
path = []
path.append(1)
while circle_array[current_index] != 1:
    # добавляем текущий элемент в путь
    path.append(circle_array[current_index])
    # перемещаем текущий индекс на следующий элемент с шагом m
    current_index = (current_index + m - 1) % n

# выводим итоговый путь
print("".join(map(str, path)))
