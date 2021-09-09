from math import sqrt
from sys import argv


circle_file = argv[1]
dot_file = argv[2]

with open (circle_file, 'r') as f:
    """Координаты центра окружности и её радиус"""
    center = [float(i) for i in f.readline().strip().split(' ')]
    radius = float(f.readline())

with open (dot_file, 'r') as f:
    """Координаты точки"""
    for line in f.readlines():
        coordinates = [float(i) for i in line.strip().split(' ')]

        coordinates[0] -= center[0]
        # X
        coordinates[1] -= center[1]
        # Y

        if coordinates[0]**2 + coordinates[1]**2 <= radius**2:
            if radius == sqrt((coordinates[0])**2 + (coordinates[1])**2):
                """Точка на окружности"""
                print(0)
            else:
                """Точка внутри"""
                print(1)
        else:
            """Точка снаружи"""
            print(2)