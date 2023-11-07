import sys

# Получаем параметры файлов из аргументов командной строки
file1 = sys.argv[1]
file2 = sys.argv[2]

# Читаем координаты центра окружности и его радиус из первого файла
with open(file1, 'r') as f:
    center_x, center_y = map(float, f.readline().split())
    radius = float(f.readline())

# Читаем координаты точек из второго файла и рассчитываем их положение относительно окружности
with open(file2, 'r') as f:
    for line in f:
        point_x, point_y = map(float, line.split())
        distance = ((point_x - center_x) ** 2 + (point_y - center_y) ** 2) ** 0.5

        if distance < radius:
            print("1")  # Точка внутри окружности
        elif distance == radius:
            print("0")  # Точка на окружности
        else:
            print("2")  # Точка снаружи окружности
